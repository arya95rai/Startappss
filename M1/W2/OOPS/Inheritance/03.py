# 4.	Create a class hierarchy for Animal, Dog, Cat, and Lion.
#  Show how common methods are inherited while child classes have their own unique methods.
class Animal:
    def superset(self):
        print("All animals")
class Dog(Animal):
    def bark(self):
        print("I am a dog and i bark")
class Cat(Animal):
    def meow(self):
        print("I am a cat and also an animal")
class Lion(Animal):
    def roar(self):
        print("I am a lion and also an animal")
obj=Lion()
obj.superset()
obj.roar()


