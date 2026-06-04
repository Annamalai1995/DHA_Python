from abc import ABC
class bus(ABC):
    def volvo(self):
        print("Luxury Bus")
class Lorry(bus):
    def volvo(self):
        print("Happy")
class Car(bus):
    def volvo(self):
        print("COstlier car")
A=bus()
A.volvo()                
l=Lorry()
l.volvo()
c=Car()
c.volvo()
