# Design an Employee class
# Attributes
# name
# department
# salary
# Methods
# login()
# apply_leave(days)
# increase_salary(amount)
# show_details()
# Requirements
# Use a constructor.
# Use instance variables (self).
# Update salary dynamically.
# Create an object and demonstrate all methods.
class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def login(self):
        print(f"Employee: {self.name}")

    def apply_leave(self,days):
        print(f"{self.name} is on leave for {self.days}")

    def increase_salary(self,amount):
        self.salary+=self.amount
        print(f"Salary increased by amount: {self.amount}")
        print(f"Updated salary: {self.salary}")

    def show_details(self):
        print(f"Employee {self.name} in {self.department} has {self.salary} salary.")
name=input("Enter employee name: ")
department=input("Enter department name: ")
salary=float(input("Enter salary: "))
obj=Employee(name,department,salary)
obj.login()
obj.apply_leave(2)
obj.increase_salary(20000)
obj.show_details()



