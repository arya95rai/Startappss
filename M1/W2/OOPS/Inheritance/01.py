# 1.	Create a Vehicle class with a start() method. 
# Create Car, Bike, and Truck classes that inherit from Vehicle and add their own methods.
class Vehicle:
    def start(self):
        print("Vehicle is starting...")
class Car(Vehicle):
    def cstart(self):
        print("Car is starting")
class Bike(Vehicle):
    def bstart(self):
        print("Bike is starting")
class Truck(Vehicle):
    def tstart(self):
        print("Truck is starting")
obj=Truck()
obj.start()
obj.tstart()


