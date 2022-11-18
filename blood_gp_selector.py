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
    return x
#Only for testing purposes
##gr,rh=split("A+")
##print(match(gr,rh))


            
            
            
        
