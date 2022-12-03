#Edit 1: Commented the create function as it's pretty useless for the time being.
#Edit 2: Commented Insert_hospital function as it has been already coded within login() function.
#Edit 3: removed Insert_Hospital Function as it's useless now.
#Edit 4: Renamed file from new_functions to Sql_functions (tbh it's only 1 function but we'll change that later asfdsgfsdf).
import mysql.connector

##def create_database():
##    try:
##        database = input("Enter database name:")
##        query = "create database {}".format(database)
##        cur.execute(query)
##        print("Database created succesfully!")
##        return database
##    except Exception:
##        print("Database already exists.")
##a = create_database()
con=mysql.connector.connect(host='localhost',user='root',passwd='root', database = "bloodbank_management",autocommit=True)
cur=con.cursor()
##def create(table):
##    try:
##        query="create table {}(Name varchar(30),Age int(4), Contact_details int(23))".format(table)
##        cur.execute(query)
##        print("Table created succesfully")
##    except Exception:
##        print("Database already exists")
#create('Gautham')
def fetch(table):
    try:
        query='select * from {}'.format(table)
        cur.execute(query)
        r=cur.fetchall()
        return r
    except Exception:
        print("Database doesnt exist")

