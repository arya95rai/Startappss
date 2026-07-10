# 1)	Create a class that overrides __str__() to display employee information.
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __str__(self):
        return f"{self.name} :  {self.id}"
obj=Employee("Arya",123)
print(obj)
