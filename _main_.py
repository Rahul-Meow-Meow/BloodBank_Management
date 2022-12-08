# Main:

import mysql.connector
con = mysql.connector.connect(host='localhost', user='root',
                              passwd='Dharmodynamics', autocommit=True)
cur = con.cursor()

try:
    query = 'create database {}'.format('bloodbank_management')
    cur.execute(query)
    con.commit()
except Exception:
    pass

from Sql_functions import *
from Hospital_Login import *
from Donor_code import *
from Recipient_code import *
import time

ch = ''

while ch not in ('e', 'E'):
    time.sleep(1)
    print ('Welcome to our Bloodbank management system!\n')
    print ('1. Register Hospital.\n')
    print ('2. Login to Hospital.\n')
    print ('3. Login to Bloodbank.\n')
    ch = \
        input('''Please select one of the above options to proceed.
                 \nPress 'E' to exit.''')
    if ch == '1':
        register()
    elif ch == '2':
        Hosp_ID = int(input('Enter Hospital ID:'))
        check(Hosp_ID)
    elif ch == '3':
        bloodbank_login()
    elif ch in ('e', 'E'):
        break
    else:
        continue
