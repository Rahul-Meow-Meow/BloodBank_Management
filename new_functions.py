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
#blood group

def split(s):
    if len(s)==2:#corresponding to O+, O-, A+, A-, B+(yeah be positive ppl),B-
        gr=s[0:1]
        rh=s[1:]
        return gr.upper(),rh
    elif len(s)==3:#corresponds to AB+ and AB-
        gr=s[0:2]
        rh=s[2:]
        return gr,rh
def match(gr,rh):
    if rh=="+":
        if gr in ["A","B"]:
            x=["O+","O-",gr+"+",gr+"-"]
        elif gr in "AB":
            x=["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    elif rh=="-":
        if gr in ["A","B"]:
            x=["O-",gr+"-"]
        elif gr=="AB":
            x=["O-","A-","B-","AB-"]
        elif gr=='O':
            x=['O-']
    return x
#Only for testing purposes
#gr,rh=split("A+")
#print(match(gr,rh))
#n=input('Enter your blood group')
#gr,rh=split(n)
#print(match(gr,rh))

#Looks legit, will be helpful. - Bharat.
#insert_hospital('employee')
