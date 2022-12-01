# Donor code

import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='Dharmodynamics',database='bloodbank_management')
cur=con.cursor()

try:
    Query ="create table {}(Full_Name varchar(50),Age int(3),Blood_Group varchar(4),Sex varchar(15),Contact_Number int(11),Address varchar(200),Amount_of_blood_donated_in_mL float(6),Date_of_donation date default(curdate()))".format('bloodbank')
    cur.execute(Query)
    con.commit()
except Exception:
    pass

def bloodbank_login():
    tries=3
    while tries>0:
        pwd=input("Enter password for login:")
        if pwd == "Dharmodynamics":
            print("Successfully logged into the Bloodbank database:")
            ch = ''
            while ch != 'n':
                print("Please select an option below:")
                print("a. Insert donor data.")
                print("b. Show list of donors.")
                ch = input("Enter an option:\nPress n to logout of the bloodbank.").lower()
                if ch == 'a':
                    bloodbank_input()
                elif ch == 'b':
                    show_don_list()
                elif ch == 'n':
                    print("Logging out...")
                    print("You have logged out.")
                    break
            break
        elif pwd!='Dharmodynamics':
            print("Incorrect password")
            tries-=1
        if tries==0:
            print("Im tired of your crap")
            break


def bloodbank_input():
    ch='y'
    count=1
    while ch=='y':
        f_name=input("Enter full name of Donor:")
        age=int(input("Enter age of Donor:"))
        bl_gr=input("Enter blood group of Donor:")
        Sex=input("Enter sex of Donor:")
        c_no=int(input("Enter contact number of Donor:"))
        address=input("Enter address of Donor:")
        req=float(input("Enter amount of blood to donate:"))
        date=int(input("Enter date:"))
        query='insert into {} values("{}",{},"{}","{}",{},"{}",{},{})'.format('bloodbank',f_name,age,bl_gr,Sex,c_no,address,req,date)
        cur.execute(query)
        con.commit()
        ch=input("Do you want to continue?(y/n):").lower()
        if ch=='y':
            count+=1
            continue
        else:
            break

def show_don_list():
    query = "select * from {}".format('bloodbank')
    cur.execute(query)
    s = cur.fetchall()
    for j in s:
        print(j)
