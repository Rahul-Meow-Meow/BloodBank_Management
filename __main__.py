#Main:

from Sql_functions import *
from Hospital_Login import *
from Donor_code import *
from Recipient_code import *

import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='root', database = 'bloodbank_management')
cur=con.cursor()

print("Welcome to our Bloodbank management system!")
print("1. Register")
print("2. Login.")
print("3. Input list of donors to the bloodbank.")
print("4. Show the list of donors.")
print("5. Show the list of recipients.")
print("6. Search for patient.")
print("7. Bridging?")

ch = ''

while ch not in ('e','E'):
    ch = input("Please select one of the above options to proceed. Press 'E' to exit.")
    if ch == '1':
        register()
    elif ch == '2':
        Hosp_ID = int(input("Enter Hospital ID:"))
        check(Hosp_ID)
    elif ch == '3':
        bloodbank_input()
    elif ch == '4':
        show_don_list()
    elif ch == '5':
        show_rec_list()
    elif ch == '6':
        Hosp_ID = int(input("Enter Hospital ID:"))
        check_patient(Hosp_ID)
    elif ch == '7':
        pass
    elif ch in ('e','E'):
        break
    else:
        continue
