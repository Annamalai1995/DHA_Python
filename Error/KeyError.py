bio={"name":['Annamalai','Gowthami','Priya','Sathish'],
     "skills":['html','Django','Flask'],
     "poc":[5,4,8,9,1],
     "salary":[5.5,10.5,6.5,8.5,9.5],
     "Company":'TCS'
     }
print(bio['name'][3])
try:
    details=input("tell us what you want")
    print(bio[details])
except KeyError as kerror:
    print(kerror)
    print("column/crdential",details,"not found") 
    
    details=input("tell us what you want")
    print(bio[details])
finally:
    print("Valid data")   
