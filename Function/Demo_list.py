#LIST
Bio=["Dhanya",4.5,50,'F']
print("List Values",Bio)
print(type(Bio))
#Adding the list new elements
#Append
Bio.append("Software developer")
print(Bio)
print(len(Bio))
#Adding new elements using insert method
Bio.insert(3,565)
print(Bio)
#Replace
Bio[5]="TeamLead"
print(Bio)
salary=[25000,65000,80000,90000]
print(min(salary))
print(max(salary))

print(sum(salary))
print(salary)
salary.remove(25000)
print(salary)
salary.pop()
print(salary)
salary.pop(1)
print(salary)
salary.reverse()
print(salary)



#List MEthod
#copy ,count
li=[25,45,55,85,44,10]
Copy=li.copy()
print(Copy)
count=li.count(55)
print(count)

# li=input("Enter the List values")
# list=li.split(",")
# print("list values")
# for i in list:
#     print(i)

#looping list
n=int(input("Enter The list"))
Empty_list=[]
for i in range(n):
    livalue=input("enter values of List")
    Empty_list.append(livalue)
print("LIST DATA",Empty_list)    
