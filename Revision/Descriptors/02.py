# Create a descriptor that stores an employee's salary.
class SalaryDescriptor:
    def __set__(self,instance,value):
        instance.__dict__["salary"]=value
    def __get__(self,instance,owner):
        return instance.__dict__["salary"]

class Employee:
    salary=SalaryDescriptor()
obj=Employee()
obj.salary=100000
print(obj.salary)
