# Syntax:
# while(condition):
#     stmts

#     Do.while:
#  do 
# {
#     print("Asmitha")
#     stmts
# }while(condition)   





#ATM PIN
# correct_pin="1234"
# Re_type=""
# while Re_type!=correct_pin:
#     Re_type=input("Enter Re_type Pin")
# print("Accessed")  

#Theater Seats:
# seat=1
# while seat <=18:
#     amount=int(input("Enter The Amount "))
#     if amount >=200:
#         print("SEAT BOOKED @",seat)
#         seat+=1
#     else:
#         print("Insufficient Balance")    

 
# hire =5
# while hire > 0:
#     skills=input("enter the skills")
#     project=int(input("How manu Project Do you have"))
#     if skills == 'python' or project >5:
#         print("You are Hired" )
#     elif skills == 'Java' or project >=10:
#         print("You are eligible to Team lead")    
#         hire-=1
#     else:
#         print("Thank you .......Tata Bye BYe")   

hire =5
while hire > 0:
    skills=input("enter the skills")
    project=int(input("How manu Project Do you have"))
    if (skills == 'python' or skills == 'java') and project >5:
        print("You are Hired" )
        hire-=1
    else: 
        print("try to upgrade Skills ")        