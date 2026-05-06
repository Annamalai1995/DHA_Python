# def Place():
#     cooling_places=input("Enter The Places")
#     if cooling_places == "OOTY":
#         print("Don't Go ooty ")
#     elif cooling_places == "Kodaikanal":
#         print("Go with family then enjoy the Ride")
#     elif cooling_places =="Coorg":
#         print("Let enjoy")  
#     else:
#         print("Stay at home")
# Place()                  

#Function With Parameter

def prompt(qual,ref):
    if qual == 'ug' and ref == 'HR':
        print("you are in us based Team")
    elif qual == 'pg' and ref == 'TeamLead':
        print("You are in Russian baseD company")
    else:
        print("You are hired")
prompt(qual='ug',ref='HR')        
prompt('ug','HR')                
prompt(ref='TeamLead',qual="pg")
prompt('pg','TeamLead')