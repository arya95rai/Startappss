# 1)	Create a Student class with an instance method to display student details
class Student:
    def __init__(self,name,age,id,class_name):
        self.name=name
        self.age=age
        self.id=id
        self.class_name=class_name
    def display(self):
        print(f"Student details: ")
        print(f"Student name: {self.name}\nAge: {self.age}\nStudent id: {self.id}\nClass: {self.class_name}")
    
s=Student("Arya Rai",23,123,"Python")
s.display()