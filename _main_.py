#Main:
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='root',autocommit=True)
cur=con.cursor()
try:
    query = "create database {}".format('bloodbank_management')
    cur.execute(query)
    con.commit()
except Exception:
    pass

from Sql_functions import *
from Hospital_Login import *
from Donor_code import *
from Recipient_code import *






ch = ''

while ch not in ('e','E'):
    print("Welcome to our Bloodbank management system!")
    print("1. Register Hospital")
    print("2. Login to Hospital.")
    print("3. Login to Bloodbank")
    ch = input("Please select one of the above options to proceed. Press 'E' to exit.")
    if ch ==    '1':
        register()
    elif ch == '2':
        Hosp_ID = int(input("Enter Hospital ID:"))
        check(Hosp_ID)
    elif ch == '3':
        bloodbank_login()
    elif ch in ('e','E'):
        break
    else:
        continue
