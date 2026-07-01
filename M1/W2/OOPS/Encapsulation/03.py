# 3. Employee Salary
# Create an Employee class.
# Private Attributes
# •	__employee_id
# •	__salary
# Methods
# •	get_salary()
# •	set_salary()
# Condition:
# •	Salary cannot be negative.
class Employee:
    def __init__(self,employee_id,salary):
        self.__employee_id=employee_id
        self.__salary=salary
    def get_salary(self):
        return self.__salary

    def set_salary(self,nsalary):
        if nsalary>=0:
            self.__salary=nsalary
        else:
            print(f"Salary cannot be negative")
employee_id=input("Enter employee id: ")
salary=float(input("Enter employee salary: "))
obj=Employee(employee_id,salary)
obj.set_salary(100000)
print(obj.get_salary())

    
