class Car:
    def Wheel(self):
        print("ALLOY WHEEELS")
class Benz(Car):
    def Luxury(self):
        print("Its a Costlier car ")
class BYD(Benz):
    def Comfort(self):
        print("BYD Compare to Benz")
b=BYD()
b.Wheel()
b.Comfort()
b.Luxury()

