# 2)	Create an abstract class Employee 
# with an abstract method calculate_salary(). 
# Implement it for FullTimeEmployee and Freelancer.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,sal):
        self.sal=sal
    def calculate_salary(self):
        return self.sal
class Freelancer(Employee):
    def __init__(self,sal):
        self.sal=sal
    def calculate_salary(self):
        return self.sal
obj=FullTimeEmployee(50000)
x=obj.calculate_salary()
print(x)             

        
