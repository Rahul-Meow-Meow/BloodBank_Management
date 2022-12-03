#Hospital Login:

#Code:
import random
import mysql.connector
from Sql_functions import *
from Blood_group_selector import *
from Donor_code import *
from Recipient_code import *

con=mysql.connector.connect(host='localhost',user='root',passwd='root',database='bloodbank_management',autocommit=True)
cur=con.cursor()

try:
    Query = "create table {}(Hospital_ID int(6), Hospital_name varchar(100), Password varchar(100))".format('hospital_list')
    cur.execute(Query)
    con.commit()
except Exception:
    pass

def input_into_hospital(Id,name,pwd):
    query="insert into hospital_list values({},'{}','{}')".format(Id,name,pwd)
    cur.execute(query)
    con.commit()

def check(Id):
    r=fetch('hospital_list')
    l=[]
    for i in r:
        l.append(i[0])
    if Id in l:
        login(Id)
    else:
        print("You havent registered with us.")
        #register()
        #r=[[1,'Rahul'],[2,'L Hopital']]
        #l=[1,2]

    
def register():
    name=input("Enter name of hospital:")
    #other details to be collected can be added later
    x=random.randrange(100000,999999)
    r=fetch('hospital_list')
    l=[]
    for i in r:
        l.append(i[0])
    if x in l:
        x=random.randrange(100000,999999)
    else:
        print("Your hospital id is:",x)
        print("Please note it down for future login")
    tries=5
    while True:
        pwd=input("Enter your password:")
        pwd2=input("Enter your password again for confirmation:")
        if pwd==pwd2:
            break
        elif pwd!=pwd2:
            print("Incorrect, try again")
            tries-=1
        if tries==0:
            print("We are done man, u arent fit to run a hospital")
            break
    input_into_hospital(x,name,pwd2)
    query='create table {} (Full_Name varchar(50),Age int(3),Blood_Group varchar(4),Sex varchar(15),Contact_Number bigint(20),Address varchar(200),Amount_of_blood_required_in_mL float(6),Date_of_request date default(curdate()))'.format('h_'+str(x))
    cur.execute(query)
    con.commit()
    
def check_patient(Id):
    n=input("Enter name of patient:")
    r = fetch('h_'+str(Id))
    l=[]
    for i in r:
        l.append(i[0])
        if n in l:
            print("Patient found:")
            print(i)
            ch = input(f"Find matches for patient {n}? y/n").lower()
            if ch == 'y':
                Match(n,Id)
            break
    else:
        print("Error 404: Patient Not Found")

def Match(n,Id):
    rhosp = fetch('h_'+str(Id))#Fetches hospital table contents
    rbank = fetch('bloodbank')#Fetches bloodbank table contents
    Rpents_n_blgrp={}
    Donors_n_blgrp = {}
    Rpents_n_req_bld = {}
    for donors in rbank:
        Donors_n_blgrp[donors[0]] = donors[2]
    
    for rpents in rhosp:
        Rpents_n_blgrp[rpents[0]] = rpents[2]
        
    for rpents in rhosp:
        Rpents_n_req_bld[rpents[0]] = rpents[6]
    
    for r_name in Rpents_n_blgrp:
        if r_name == n:
            bl_grp = Rpents_n_blgrp[r_name]
            gr,rh=Split(bl_grp)
            matched_bl_grps = b_match(gr,rh)# List of the possible blood groups that can donate.
            list_o_donors = []
            for d_names in Donors_n_blgrp:
                if Donors_n_blgrp[d_names] in matched_bl_grps:
                    list_o_donors.append(d_names)
                    
            for d_name in list_o_donors:
                for donors in rbank:
                    if donors[0] == d_name:
                        print("Possible Donors:")
                        print(donors)
            don_choice = input("Enter your choice of donor:")
            
##            for donors in rbank:
##                if donors[0] == don_choice:
##                    tup = donors
        
            for d_name in list_o_donors:
                if don_choice == d_name:
                    req_bld_amt = Rpents_n_req_bld[n]
                    #print(req_bld_amt)
                    for donors in rbank:
                        if donors[0] == d_name:
                            if donors[6]<req_bld_amt:
                                rem_rec_bld_amt=req_bld_amt-donors[6]
                                rem_don_bld_amt=0
                                query='update {} set  Amount_of_blood_donated_in_mL = {} where Full_Name="{}"'.format('bloodbank',rem_don_bld_amt,d_name)
                                query2 = 'update {} set Amount_of_blood_required_in_mL = {} where Full_Name="{}"'.format('h_'+str(Id),rem_rec_bld_amt,n)
                                print(f"{rem_rec_bld_amt} is still remaining to be given, please give the remaining blood")
                                cur.execute(query)
                                con.commit()
                                cur.execute(query2)
                                con.commit()
##                                break_out_Flag=True
##                                break
                            else:
                                rem_don_bld_amt = donors[6] - req_bld_amt
                                rem_rec_bld_amt = 0
                                print("Successfully requested for the donated blood!!")
                                query='update {} set  Amount_of_blood_donated_in_mL = {} where Full_Name="{}"'.format('bloodbank',rem_don_bld_amt,d_name)
                                query2 = 'update {} set Amount_of_blood_required_in_mL = {} where Full_Name="{}"'.format('h_'+str(Id),rem_rec_bld_amt,n)              
                                cur.execute(query)
                                con.commit()
                                cur.execute(query2)
                                con.commit()

##def new_Match(n,Id):
##    rhosp = fetch('h_'+str(Id))#Fetches hospital table contents
##    rbank = fetch('bloodbank')#Fetches bloodbank table contents
##    Rpents_n_blgrp={}
##    Donors_n_blgrp = {}
##    Rpents_n_req_bld = {}
##    for donors in rbank:
##        Donors_n_blgrp[donors[0]] = donors[2]
##    
##    for rpents in rhosp:
##        Rpents_n_blgrp[rpents[0]] = rpents[2]
##        
##    for rpents in rhosp:
##        Rpents_n_req_bld[rpents[0]] = rpents[6]
##    
##    for r_name in Rpents_n_blgrp:
##        if r_name == n:
##            bl_grp = Rpents_n_blgrp[r_name]
##            gr,rh=Split(bl_grp)
##            matched_bl_grps = b_match(gr,rh)# List of the possible blood groups that can donate.
##            list_o_donors = []
##            for d_names in Donors_n_blgrp:
##                if Donors_n_blgrp[d_names] in matched_bl_grps:
##                    list_o_donors.append(d_names)
##                    
##            for d_name in list_o_donors:
##                print("Possible Donors:")
##                for donors in rbank:
##                    if donors[0] == d_name:
##                        print(donors)
##                        print()
##            don_choice = input("Enter your choice of donor:")
##            if don_choice in list_o_donors:
##                req_bld_amt = Rpents_n_req_bld[n]
##                        #print(req_bld_amt)
##            while req_bld_amt>=0:
##    ##            for donors in rbank:
##    ##                if donors[0] == don_choice:
##    ##                    tup = donors
##                for donors in rbank:
####                    print(donors[0])
####                    print()
####                    print(d_name)
##                    if donors[0]==don_choice:
##                        if donors[6]<req_bld_amt and donors[6]!=0:
##                            #print(donors)
##                            #print("Donor has less blood than required")
##                            rem_bld_amt=req_bld_amt-donors[6]
##                            #don_bld_amt=donors[6]
##                            print("Successfully requested for the donated blood!!")
##                            print(f"Remaining amount of blood needed is {rem_bld_amt}")
##                            query='update {} set  Amount_of_blood_donated_in_mL = {} where Full_Name="{}"'.format('bloodbank',rem_bld_amt,d_name)
##                            query2 = 'update {} set Amount_of_blood_required_in_mL = {} where Full_Name="{}"'.format('h_'+str(Id),donors[6],n)              
##                            cur.execute(query2)
##                            con.commit()
##                            cur.execute(query)
##                            con.commit()
##                            req_bld_amt=-1
##                            continue
##                        elif donors[6]==0:
##                            print(donors)
##                            print("Donor has no blood")
##                            print("There is no more blood idiot")
##                            #don_choice = input("Enter your choice of donor:")
##                                    
####                                    pass
##                            break
##                        elif donors[6]>=req_bld_amt:
##                            print("Donor has more blood than req")
##                            rem_bld_amt=donors[6]-req_bld_amt
##                            don_bld_amt=req_bld_amt
##                            print("Successfully requested for the donated blood!!")
##                            print(f"Remaining amount of blood needed is 0")
##                            query='update {} set  Amount_of_blood_donated_in_mL = {} where Full_Name="{}"'.format('bloodbank',rem_bld_amt,d_name)
##                            query2 = 'update {} set Amount_of_blood_required_in_mL = 0 where Full_Name="{}"'.format('h_'+str(Id),n)              
##                            cur.execute(query2)
##                            con.commit()
##                            cur.execute(query)
##                            con.commit()
##                            req_bld_amt=-1
##                            break
                            

                        
                        

##    for i in r:
##        if i[0] == n:
##            b=i[2]
##            gr,rh=Split(b)
##            l=b_match(gr,rh)
##            return l

               
def login(Id):
    #Id=int(input("Enter Hospital id:"))
    r=fetch('hospital_list')
    l=[]
    for i in r:
        l.append(i[0])
    d={}
    for i in r:
        d[i[0]]=i[2]
    tries=3#if u type the wrong password for 3 times, the loop breaks
    while True: 
        pwd=input("Enter password for login:")
        if pwd==d[Id]:
            print("You've successfully logged into your account.")
            print(f"Hospital ID: {Id}")
            for i in r:
                if i[0] == Id: 
                    print(f"Hospital Name: {i[1]}")
            cho = ''
            while cho !='no':
                print("Select one of the following options:")
                print("a. Insert recipient data.")
                print("b. Show the list of recipients.")
                print("c. Match group for recipient and make donation.")
                cho = input("Select your choice: \nType 'no' to Logout.").lower()
                if cho == 'a':
                    insert_rec_data(Id)
                elif cho == 'b':
                    show_rec_list(Id)
                elif cho == 'c':
                    check_patient(Id)
                elif cho == 'no':
                    print("You have logged out.")
                    break
                else:
                    continue
            break
        elif pwd!=d[Id][0]:
            print("Incorrect password")
            tries-=1
        if tries==0:
            print("Im tired of your crap")
            break

##def display_records(Id):
##    r=fetch('hospital_list')
##    print("Records of the hospital are:")
##    print(fetch('h_'+str(Id)))  

def insert_rec_data(Id):
    r=fetch('hospital_list')
    ch='y'
    count=1
    while ch=='y':
        f_name=input("Enter full name of Recipient:")
        age=int(input("Enter age of Recipient:"))
        bl_gr=input("Enter blood group of Recipient:")
        Sex=input("Enter sex of Recipient:")
        c_no=int(input("Enter contact number of Recipient:"))
        address=input("Enter address of Recipient:")
        req=float(input("Enter amount of blood required:"))
        date=int(input("Enter date:"))
        query='insert into {} values("{}",{},"{}","{}",{},"{}",{},{})'.format('h_'+str(Id),f_name,age,bl_gr,Sex,c_no,address,req,date)
        cur.execute(query)
        con.commit()
        ch=input("Do you want to continue?(y/n):").lower()
        if ch=='y':
            count+=1
            continue
        else:
            break
                     
