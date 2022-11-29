import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='Dharmodynamics',database='bloodbank_management')
cur=con.cursor()

try:
    Query ="create table {}(Full_Name varchar(50),Age int(3),Blood_Group varchar(4),Sex varchar(15),Contact_Number int(11),Address varchar(200),Amount_of_blood_donated_in_mL float(6),Date_of_donation date default(curdate()))".format('bloodbank')
    cur.execute(Query)
    con.commit()
except Exception:
    pass


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
