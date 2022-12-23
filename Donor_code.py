# Donor code

import time
import mysql.connector
import json

con = mysql.connector.connect(host='localhost', user='root',passwd='root', 
                              database = 'bloodbank_management',autocommit=True)
cur = con.cursor()

try:
    Query = '''create table {}(Full_Name varchar(50),Age int(3),
                Blood_Group varchar(4),
                Sex varchar(15),
                Contact_Number bigint,
                Address varchar(200),
                Amount_of_blood_donated_in_mL float(6),
                Date_of_donation date default(curdate()))'''.format("bloodbank")
    cur.execute(Query)
    con.commit()
except Exception:
    pass


def bloodbank_login():
    tries = 3
    while tries > 0:
        pwd = input("Enter password for login:")
        if pwd == "peopleservice":
            time.sleep(1.25)
            print('''Successfully logged into the Bloodbank database!\n\n''')
            ch = ""
            while ch != "n":
                print("Please select an option below:")
                print("a. Insert donor data.\n")
                print("b. Show list of donors.\n")
                ch = input('''Enter an option.
                           \nPress n to logout of the bloodbank:\n''').lower()
                
                if ch == "a":
                    bloodbank_input()
                elif ch == "b":
                    show_don_list()
                elif ch == "n":
                    print("Logging out...\n")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print('''You have logged out.
                             \nRedirecting you to the main menu.\n\n''')
                    time.sleep(1)
                    break
            break
        elif pwd != "peopleservice":
            time.sleep(0.75)
            print("Incorrect password!! Try again.")
            tries -= 1
        if tries == 0:
            print('''Too many login failures. Please try again sometime.
                    \nRedirecting you to the main menu\n\n''')
            time.sleep(1)
            break


def bloodbank_input():
    ch = "y"
    count = 1
    while ch == "y":
        f_name = input("Enter full name of Donor:")
        while True:
            try:
                age = int(input("Enter age of Recipient:"))
            except Exception:
                print("Please enter a valid age.")
                continue
            else:
                break
        while True:
            bl_gr = input("Enter blood group of Recipient:")
            if bl_gr not in ["A+","B+","O+","A-","B-","O-","AB+","AB-"]:
                print("Please enter a valid blood group.")
                continue
            else:
                break
        Sex=input("Enter sex of Donor:")
        while True:
            try:
                c_no = int(input("Enter contact number of Recipient:"))
            except Exception:
                print("Please enter a valid contact number.")
            else:
                break
        address=input("Enter address of Donor:")
        while True:
            try:
                req = float(input("Enter amount of blood required:"))
            except Exception:
                print("Please enter a valid input.")
            else:
                break
        while True:
            try:
                date = int(input("Enter date in YY-MM-DD format:"))
            except Exception:
                print("Please enter a valid date. YY-MM-DD.")
                continue
            else:
                break
        query = '''insert into {} values
                   ("{}",{},"{}","{}",{},"{}",{},{})'''.format("bloodbank", f_name,
                                                               age, bl_gr, Sex,
                                                               c_no, address,
                                                               req, date)
        cur.execute(query)
        con.commit()
        time.sleep(1.5)
        ch = input("Do you want to continue?(y/n):").lower()
        if ch == "y":
            time.sleep(1)
            count += 1
            continue
        else:
            break


def show_don_list():
    query = "select * from {}".format("bloodbank")
    cur.execute(query)
    s = cur.fetchall()
    print("List of Donors:")
    if len(s) == 0:
        print("There are no donors.")
    for j in s:
        d = dict(
            zip(
                [
                    "Full Name",
                    "Age",
                    "Blood Group",
                    "Sex",
                    "Contact Number",
                    "Address",
                    "Amount of blood donated in mL",
                    "Date_of_donation",
                ],
                j,
            )
        )
        time.sleep(1)
        print(json.dumps(d, indent=4, default=str))

