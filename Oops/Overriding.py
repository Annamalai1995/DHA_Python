class Payment:
    def pay(self,amount):
        print(f"Paying,{amount}")
class creditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} credit card") 
class Upi(Payment):
    def pay(self,amount):
        print(f"Paid {amount} UPI MODE")
Payment=[creditCard(),Upi()]

for a in Payment:
    a.pay(5000)
             
class Dhanya:
    def name(self):
        print("Dhanya cluny")
class Asmitha(Dhanya):
    def name(self):
        super().name()
        print("Asmitha cluny")    
class Aswathi(Asmitha):
    def name(self):
        super().name()
        print("Aswathi cluny")
class Aishwarya(Aswathi):
    def name(self):
        super().name()
        print("Aishwarya cluny")        
A=Aishwarya()
dA.name()  
#A.name()      
