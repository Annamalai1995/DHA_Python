class College:
    def __init__(self,Name,Course):
        self.n=Name
        self.c=Course
    def display(self):
        print(self.n,self.c)
c=College("Karpagam","BE CSE")

c.display()        