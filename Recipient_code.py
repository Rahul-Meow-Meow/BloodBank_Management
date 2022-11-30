import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='root',database='bloodbank_management')
cur=con.cursor()
from Hospital_Login import *
from Sql_functions import *


##Hosp_ID = int(input("Enter Hospital ID:"))
##check(Hosp_ID)

def show_rec_list():
    print("Select Hospital ID of your choice:")
    query = "select Hospital_ID from {}".format("hospital_list")
    cur.execute(query)
    r=cur.fetchall()
    for i in r:
        for j in i:
            print(f"- h_{j}")
    choice = int(input("...\n"))
    for i in r:
        if choice == i[0]:
            print('yes')
            query = "select * from {}".format('h_'+str(choice))
            cur.execute(query)
            s = cur.fetchall()
            for j in s:
                print(j)
            n=input("Enter name of person:")
            Match(n,choice)
#Not much of a change, just changed the name to Recipient_code since this was for recipients all along.
