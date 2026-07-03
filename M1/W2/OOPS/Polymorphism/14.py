# 14.	Demonstrate method overriding using an Animal class and Dog and Cat subclasses.
class Animal:
    def sound(self):
        print("Animal sounds: ")
class Dog(Animal):
    def sound(self):
        print("Bhaw")
class Cat(Animal):
    def sound(self):
        print("Meow")
d=Dog()
c=Cat()
animal=[d,c]
for i in animal:
    i.sound()