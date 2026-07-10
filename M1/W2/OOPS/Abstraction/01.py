# 1)	Create an abstract class Vehicle with an abstract method start(). 
# Implement it in Car and Bike.
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
obj=Car()
obj1=Bike()
obj.wheels()
obj1.wheels()


