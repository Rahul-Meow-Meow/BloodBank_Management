import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='root',database='bloodbank_management',autocommit=True)
cur=con.cursor()
from Hospital_Login import *
from Sql_functions import *


##Hosp_ID = int(input("Enter Hospital ID:"))
##check(Hosp_ID)

def show_rec_list(Id):
    query = "select Hospital_ID from {}".format("hospital_list")
    cur.execute(query)
    r=cur.fetchall()
    for i in r:
        if Id == i[0]:
            print('List of Recipients:')
            query = "select * from {}".format('h_'+str(Id))
            cur.execute(query)
            s = cur.fetchall()
            for j in s:
                print(j)
