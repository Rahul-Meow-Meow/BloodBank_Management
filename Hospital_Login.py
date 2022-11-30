#Hospital Login:

#Code:
import random
import mysql.connector
from Sql_functions import *
from Blood_group_selector import *
con=mysql.connector.connect(host='localhost',user='root',passwd='root',database='bloodbank_management')
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
            Match(n,Id)
            break
    else:
        print("Error 404: Patient Not Found")

def Match(n,Id):
    r1=fetch('h_'+str(Id))
    r=fetch('bloodbank')
    #print(r)
    d1={}
    d={}
    d_nomore={}
    for j in r:
        d[j[0]]=j[2]
    #print(d)
    for new in r1:
        d1[new[0]]=new[2]
    for very_new in r1:
        d_nomore[very_new[0]]=very_new[6]
##    print()
##    print(d1)
    #for i in r:
    for c in d1:
        if c == n:
            b=d1[c]
            #print(b)
            gr,rh=Split(b)
            l=b_match(gr,rh)
            l2=[]
            #
            for k in d:
                if d[k] in l:
                    l2.append(k)
            #print(l2)
            for z in l2:
                for variable in r:
                    #l3=[]
                    if variable[0]==z:
                        print(variable)
                        #l3.append(variable)
            x=input("Enter your choice of donor:")
            for A in r:
                if A[0]==x:
                    tup=A
            print(l2)   
            for f in l2:
                #print(f)
                if x==f:
                    change=d_nomore[n]
                    print(change)
                    #t=type_cast(tup,6,change)
                    for FINAL in r:
                        if FINAL[0]==f:
                            remain=FINAL[6]-change
                            query='update {} set  Amount_of_blood_donated_in_mL = {} where Full_Name="{}"'.format('bloodbank',remain,f)
                            cur.execute(query)
                            con.commit()
##                            print(FINAL)
##                            t=type_cast(FINAL,6,change)
##                            INDD=r.index(FINAL)
##                            r.pop(INDD)
##                            r.insert(INDD,t)
##                    print("Changed list")
##                    print(r)
                            
                            
                    #r1.pop(IND)
                    #r1.append(t)
            #print(r1)
                                
##                    
##def type_cast(t,index,change):
##    l=list(t)
##    #print(l[index])
##    l[index]=l[index]-change
##    t1=tuple(l)
##    return t1
         
    
                    
                    
                    
##            query='select * from {} where Blood_Group like "{}" or "{}" or "{}" or "{}" or "{}" or "{}" or "{}" or "{}"'.format('bloodbank',a,b,c,d,e,f,g,h)
##            l=cur.execute(query)
##            r=l.fetchall()
##            print(r)
            
            
            

               
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
