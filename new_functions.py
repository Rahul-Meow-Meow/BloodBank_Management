import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='root',database='hello')
cur=con.cursor()
def create(table):
    try:
        query="create table {}(Name varchar(30),Age int(4), Contact_details int(23))".format(table)
        cur.execute(query)
        print("Table created succesfully")
    except Exception:
        print("Database already exists")
#create('Gautham')
def fetch(table):
    try:
        query='select * from {}'.format(table)
        cur.execute(query)
        r=cur.fetchall()
        return r
    except Exception:
        print("Database doesnt exist")

#print(display('employee'))
#create('Hello2')
#print(fetch('employee'))
def insert_hospital(table):
    n=int(input("Enter number of donors:"))
    try:
        for i in range(0,n):
            sno=int(input("Enter serial number"))
            name=input("Enter name:")
            age=input("Enter age:")
            c_no=int(input("Enter Phone number of person:"))
            query='insert into {} values("{}","{}",{},{})'.format(table,sno,name,age,c_no)
            cur.execute(query)
            con.commit()
    except Exception:
        print("Database not found")
#insert_hospital('employee')
