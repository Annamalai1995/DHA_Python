# Name=("Asmitha","Aswathi","Dhanya","Aishwarya")
# print(Name)
# print(type(Name))

#SLicing
# print(Name[0:3])
# print(Name[:2])

#Tuple methods
# values=(145,45,55,68,95,1052)
# values1=values.count(145)
# print(values1)
# data=values.index(55)
# print(data)

#APpend MEthod
# college=('Psg','Kct','Karpagam','Gce')
# college1=list(college)
# college1.append('kiot')
# college=tuple(college1)
# print(college)

#Adding Tuple to Tuple
data=('Aishwarya','Dhanya','Aswathi')
data1=('Asmitha',)
data+=data1
print(data)

#join
place=('coorg','Ooty','Manali')
places=(123,45,66)
result=place+places
print(result)
#Join
place=('coorg','Ooty','Manali')
join=place*4
print(join)

#range
a=(12,45,'pk','sam')
for i in range(len(a)):
    print(a[i])

for i in a:
    print(a)
    