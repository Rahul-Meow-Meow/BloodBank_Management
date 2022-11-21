#Donor
#Meow
import json

def donor_data():
    d = {}
    
    Sno = 0
    good_d = ''
    while True:
        do_nme = input("Enter full name of the donor:")
        do_age = int(input("Enter age of the donor:"))
        do_gen = ""
        while do_gen not in ["M", "F"]:
            do_gen = input("Sex of donor {M/F}:").upper()
            continue
        Bl_grp = input("Enter blood group of donor:")
        do_cntct = 0
        while len(str(do_cntct)) !=10:
            do_cntct = int(input("Enter contact no. of the donor:"))
            continue
        do_addr = input("Enter address of the donor:")
        qty_bld = float(input("Enter quantity of blood in mililitres (ml):"))
        dte_o_donr = input("Enter date of donation: YYYY-MM-DD")
        d[f"Donor {Sno+1}"] = {"Name":do_nme, "Age":do_age, "Sex":do_gen, "Blood group":Bl_grp, "Contact no.":do_cntct, "Address":do_addr, "Blood Donated (in Litres)":qty_bld, "Date of donation":dte_o_donr}
        good_d = json.dumps(d, sort_keys = False, indent = 4)
        addmore = int(input("Press 1 to continue adding more donors. Press any other key to stop"))
        if addmore == 1:
            Sno+=1
            continue
        else:
            break
    return good_d

def dsply_donr_data():
    Donor_data = donor_data()
    print(Donor_data)


dsply_donr_data()
#One more trial-Rahul
