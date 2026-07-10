# 2)	Create an Employee class with a 
# class variable company and a class method to update it.
class Employee:
    company="Startappss"
    def __init__(self,name):
        self.name=name
       
    @classmethod
    def upd(cls,up):
        cls.company=up
c=Employee("arya")
c.upd("Morgan")
print(c.company)