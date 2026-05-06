#Function with Default Arguments

#def func_name(parameter='')

def register(name,location,prefix="Mr/Mrs/Miss"):
    if location == 'Salem':
        print(prefix,name,"Has Approved in",location)
    elif location == 'Chennai':
        print(prefix,name,'Relocate the chennai branch',location)
    else:
        print("Business Not Approved")        
register("zealous Tech corp","Salem")  
register('GP Transport','Chennai','Mr.')
register("Completed",'Priya') 




#Banking
balance=[20000,1000,500,10000]
def debit(money=0,pos=0):
    if money <= balance[pos]:
        balance[pos]-=money
        print(money,"Balance")
        return balance[pos]
    else:print("cannot Debit")
bank=debit(100,1)
debit(bank)    