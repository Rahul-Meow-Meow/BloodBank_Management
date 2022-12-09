# blood group


def Split(s):
    if len(s) == 2:  # corresponding to O+, O-, A+, A-, B+, B-
        gr = s[0:1]
        rh = s[1:]
        return gr.upper(), rh
    elif len(s) == 3:  # corresponds to AB+ and AB-
        gr = s[0:2]
        rh = s[2:]
        return gr, rh


def b_match(gr, rh):
    if rh == "+":
        if gr in ["A", "B"]:
            x = ["O+", "O-", gr + "+", gr + "-", " ", " ", " ", " "]
        elif gr in "AB":
            x = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
        elif gr in "O":
            x = ["O+", "O-", " ", " ", " ", " ", " ", " "]
    elif rh == "-":
        if gr in ["A", "B"]:
            x = ["O-", gr + "-", " ", " ", " ", " ", " ", " "]
        elif gr == "AB":
            x = ["O-", "A-", "B-", "AB-", " ", " ", " ", " "]
        elif gr == "O":
            x = ["O-", " ", " ", " ", " ", " ", " ", " "]
    return x
            
            
            
        

            
            
        
