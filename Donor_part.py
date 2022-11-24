import mysql.connector
from new_functions import *
con=mysql.connector.connect(host='localhost',user='root',passwd='root',database='hello')
cur=con.cursor()
#login
import random
#d={123231: ["Password","Meow Hospitals"], 123345: ["Random Password","Not Meow Hospitals"]}
def input_into_hospital(Id,name,pwd):
    query="insert into hospital_list values({},'{}','{}')".format(Id,name,pwd)
    cur.execute(query)
    con.commit()
def check(Id):
    r=fetch('hospital_list')
    l=[]
    for i in r:
        l.append(i[0])
    if Id in l:
        login(Id)
    else:
        print("You havent registered with us")

        register()
        #r=[[1,'Rahul'],[2,'L Hopital']]
        #l=[1,2]
    
    
def register():
    name=input("Enter name of hospital:")
    #other details to be collected can be added later
    x=random.randrange(100000,999999)
    r=fetch('hospital_list')
    l=[]
    for i in r:
        l.append(i[0])
    if x in l:
        x=random.randrange(100000,999999)
    else:
        print("Your hospital id is:",x)
        print("Please note it down for future login")
    tries=5
    while True:
        pwd=input("Enter your password:")
        pwd2=input("Enter your password again for confirmation:")
        if pwd==pwd2:
            break
        elif pwd!=pwd2:
            print("Incorrect, try again")
            tries-=1
        if tries==0:
            print("We are done man, u arent fit to run a hospital")
            break
    input_into_hospital(x,name,pwd2)
    query='create table {} (Full_Name varchar(50),Age int(3),Blood_Group varchar(4),Sex varchar(15),Contact_Number int(10),Address varchar(200),Amount_of_blood_donated_in_mL float(6),Date_of_donation date default(curdate()))'.format('h_'+str(x))
    cur.execute(query)
    con.commit()
    
        
    
    
def login(Id):
    #Id=int(input("Enter Hospital id:"))
    r=fetch('hospital_list')
    l=[]
    for i in r:
        l.append(i[0])
    d={}
    for i in r:
        d[i[0]]=i[2]
    tries=3#if u type the wrong password for 3 times, the loop breaks
    while True: 
        pwd=input("Enter password for login:")
        if pwd==d[Id]:
            print("Records of the hospital are:")
            print(fetch('h_'+str(Id)))
            ch='y'
            count=1
            while ch=='y':
                f_name=input("Enter full name of recepient:")
                age=int(input("Enter age of recepient:"))
                bl_gr=input("Enter blood group of recepient:")
                Sex=input("Enter sex of recepient:")
                c_no=int(input("Enter contact number of recepient:"))
                address=input("Enter address of recepient:")
                req=float(input("Enter amount of blood required:"))
                date=int(input("Enter date:"))
                query='insert into {} values("{}",{},"{}","{}",{},"{}",{},{})'.format('h_'+str(Id),f_name,age,bl_gr,Sex,c_no,address,req,date)
                cur.execute(query)
                con.commit()
                ch=input("Do you want to continue?(y/n):").lower()
                if ch=='y':
                    count+=1
                    continue
                else:
                    break
                
                
            #ofc ntg will be printed, but imagine this to be a database with all info
##                print(d[Id])
            
            break
        elif pwd!=d[Id][0]:
            print("Incorrect password")
            tries-=1
        if tries==0:
            print("Im tired of your crap")
            break
##    if Id not in d:
##        ch=int(input('''If you entered the Id wrong, press 1
##If you havent registered with the blood bank, press 2:'''))
##        if ch==1:
##               Id=int(input("Enter hospital id:"))
##        if ch==2:
##               register()
#login()  

n=int(input("Enter hospital Id:"))
check(n)






