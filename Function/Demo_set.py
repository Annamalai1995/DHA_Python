name={'Aswathi','Dhanya','Aishwarya','Asmitha','Dhanya'}
print(name)

#set constructor
place=set(('salem','Chennai',"Pondy"))
print(place)

#update set
alpha={'kumar','Raja','Deepika','Sathish'}
alpha.update('Mani')
print(alpha)

#update Set
a={'Coorg','Manali','Ooty','Kodaikanal'}
li=['Hari']
a.update(li)
print(a)

#remove Set
a={1,2,3,"sam","pk"}
a.remove("sam")
print(a)
a.discard(2)

print(a)

 
#pop method
s={"sam","pk","sathish","viji" }
s1=s.pop()
print(s1)
print(s)



#Access Set
a={"sam","pk","anu","sathish"}
for i in a:
    print(i)

#check the set is present or not
a={"sam","pk","anu","sathish"}
print("pk" in a)





