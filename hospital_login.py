#login
import random
d={123231: ["Password","Meow Hospitals"], 123345: ["Random Password","Not Meow Hospitals"]}

def register():
    name=input("Enter name of hospital:")
    #other details to be collected can be added later
    x=random.randrange(100000,999999)
    if x in d:
        x=random.randrange(100000,999999)
    else:
        print("Your hospital id is:",x)
        print("Please note it down for future login")
    tries=5
    while True:
        pwd=input("Enter your password:")
        pwd2=input("Enter your password again for verification:")
        if pwd==pwd2:
            break
        elif pwd!=pwd2:
            print("Incorrect, try again")
            tries-=1
        if tries==0:
            print("We are done man, u arent fit to run a hospital")
            break
    d[x]=[pwd,name]
    
        
    
    
def login():
    Id=int(input("Enter Hospital id:"))
    if Id in d:
        tries=3#if u type the wrong password for 3 times, the loop breaks
        while True: 
            pwd=input("Enter password:")
            if pwd==d[Id][0]:
                print("Records of the hospital are:")#ofc ntg will be printed, but imagine this to be a database with all info
                print(d[Id])
                break
            elif pwd!=d[Id][0]:
                print("Incorrect password")
                tries-=1
            if tries==0:
                print("Im tired of your crap")
                break
    if Id not in d:
        ch=int(input('''If you entered the Id wrong, press 1
If you havent registered with the blood bank, press 2:'''))
        if ch==1:
               Id=int(input("Enter hospital id:"))
        if ch==2:
               register()
login()  
    
                     
