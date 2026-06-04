class Animal:
    def speak(self):
        print("Animal sound is louder")
class Cat(Animal):
    def speak(self):
        print("meaow")
class Dog(Animal):
    def speak(self):
        print("Dogs")
C=Cat()
D=Dog()
C.speak()
D.speak()
