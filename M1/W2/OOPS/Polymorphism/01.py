# 11.	Create Dog, Cat, and Cow classes with a sound() method. 
# Use a loop to demonstrate runtime polymorphism.
class Dog:
    def sound(self):
        print("bhaw bhaw")
class Cat:
    def sound(self):
        print("meow meow")
class Cow:
     def sound(self):
        print("moo moo")
def make_sound(animal):
    animal.sound()
d=Dog()
c=Cat()
co=Cow()
animal=[d,c,co]
for i in animal:
    print(make_sound(i))