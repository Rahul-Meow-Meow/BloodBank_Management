#Hospital Login:

#Code:
import random
import mysql.connector
from Sql_functions import *
from Blood_group_selector import *
con=mysql.connector.connect(host='localhost',user='root',passwd='Dharmodynamics',database='bloodbank_management')
cur=con.cursor()

try:
    Query = "create table {}(Hospital_ID int(6), Hospital_name varchar(100), Password varchar(100))".format('hospital_list')
    cur.execute(Query)
    con.commit()
except Exception:
    print("We move.")

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
        print("You havent registered with us.")
        #register()
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
    query='create table {} (Full_Name varchar(50),Age int(3),Blood_Group varchar(4),Sex varchar(15),Contact_Number int(20),Address varchar(200),Amount_of_blood_required_in_mL float(6),Date_of_request date default(curdate()))'.format('h_'+str(x))
    cur.execute(query)
    con.commit()
    
def check_patient(Id):
    n=input("Enter name of patient:")
    r = fetch('h_'+str(Id))
    l=[]
    for i in r:
        l.append(i[0])
        if n in l:
            #print("Boy I'm boutta whip yo pickle chin ah boy")
            matched_bgr = Match(n,Id)
            print(f"Possible matches: {matched_bgr}")
            break
    else:
        print("Error 404: Patient Not Found")

def Match(n,Id):
    r=fetch('h_'+str(Id))
    for i in r:
        if i[0] == n:
            b=i[2]
            gr,rh=Split(b)
            l=b_match(gr,rh)
            return l

               
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
                f_name=input("Enter full name of Recipient:")
                age=int(input("Enter age of Recipient:"))
                bl_gr=input("Enter blood group of Recipient:")
                Sex=input("Enter sex of Recipient:")
                c_no=int(input("Enter contact number of Recipient:"))
                address=input("Enter address of Recipient:")
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
            break
        elif pwd!=d[Id][0]:
            print("Incorrect password")
            tries-=1
        if tries==0:
            print("Im tired of your crap")
            break
    
#Edit - 1 Changed file name from hospital_list to Hospital_List
#Edit - 2 Commented register under check function as we can ask the user to register separately.
#Edit - 3 Added check_patient() function.
#Edit - 4 Upgraded check_patient() function.
#Edit - 5 Added Match() function
#Edit - 6 Upgraded Match() function.
#Edit - 7 Login accepts data from the RECIPIENT AKA THE PATIENT.
#Edit - 8 Rahul GOAT.
