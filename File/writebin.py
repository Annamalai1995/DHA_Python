from pickle import *
name=open("Annamalai.txt",'wb')
frnds=['Sathish','Gowthami','vidhya','Mani']
college={"Name":"Karpagam","Dept":"BE CSE"}
location=("coimbatore","salem")

dump(frnds,name)
dump(college,name)
dump(location,name)
name.close()
