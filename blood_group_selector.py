#blood group

def Split(s):
    if len(s)==2:#corresponding to O+, O-, A+, A-, B+(yeah be positive ppl),B-
        gr=s[0:1]
        rh=s[1:]
        return gr.upper(),rh
    elif len(s)==3:#corresponds to AB+ and AB-
        gr=s[0:2]
        rh=s[2:]
        return gr,rh
def b_match(gr,rh):
    if rh=="+":
        if gr in ["A","B"]:
            x=["O+","O-",gr+"+",gr+"-",'random','random','random','ransom']
        elif gr in "AB":
            x=["O+","O-","A+","A-","B+","B-","AB+","AB-"]
        elif gr in "O":
            x=["O+","O-",'random','random','random','ransom''random','random']
    elif rh=="-":
        if gr in ["A","B"]:
            x=["O-",gr+"-",'random','random','random','ransom''random','random']
        elif gr=="AB":
            x=["O-","A-","B-","AB-"'random','random','random','ransom']
        elif gr=='O':
            x=['O-','random','random','random','ransom','random','random','random']
    return x
#Only for testing purposes
##gr,rh=Split("A+")
##print(b_match(gr,rh))
##n=input('Enter your blood group')
##gr,rh=Split(n)
##print(b_match(gr,rh))

#Looks legit, will be helpful. - Bharat.
            
            
        
