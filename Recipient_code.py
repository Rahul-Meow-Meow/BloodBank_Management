import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', passwd='root', 
                              database = 'bloodbank_management', autocommit=True)

cur = con.cursor()

from Hospital_Login import *

from Sql_functions import *

import time

import json


def show_rec_list(Id):
    print ('List of Recipients:')
    query2 = 'select * from {}'.format('h_' + str(Id))
    cur.execute(query2)
    s = cur.fetchall()
    if len(s) == 0:
        print("There are no recipients.")
    for j in s:
        d = dict(zip([
            'Full Name',
            'Age',
            'Blood Group',
            'Sex',
            'Contact Number',
            'Address',
            'Amount of blood requested in mL',
            'Date_of_request',
            ], j))
        time.sleep(1)
        print (json.dumps(d, indent=4, default=str))



        
