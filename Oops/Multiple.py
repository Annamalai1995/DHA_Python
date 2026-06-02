class Travels:
    def busname(self):
        print("Swamy Ayyappa")
class Travels1:
    def bustype(self):
        print("VOlvo 9600 SLX")

class main_class(Travels,Travels1):
    def Price(self):
        print("3500RS")
M=main_class()
M.busname()
M.bustype()
M.Price()


        