# 4.Create a Driver and Car class where a driver drives a car, 
# but both objects can exist independently.
class Driver:
    def __init__(self,name):
        self.name=name
class Car:
    def __init__(self,model):
        self.model=model
        self.driver=None
    def assign_driver(self,driver):
        self.driver=driver
    
    def details(self):
        print(f"Model of car: {self.model}")
        if self.driver:
            print(f"Name of driver: {self.driver.name}")
        else:
            print("No driver assigned")
d=Driver("Arya")
c=Car(456)
c.assign_driver(d)
c.details()

