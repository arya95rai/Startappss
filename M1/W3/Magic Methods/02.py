# 2)	Create a class that overrides __repr__() for debugging.
class Student:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"Student(name= '{self.name}')"
s=Student("Arya Rai")
print(s)
print(repr(s)) 