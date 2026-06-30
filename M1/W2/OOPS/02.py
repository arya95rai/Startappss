# Create a Student class
# Attributes (4)
# student_id
# name
# age
# marks
# Methods (5)
# study()
# take_exam()
# show_result()
# show_profile()
# update_marks()
# Requirements
# Use a constructor (__init__).
# Use self correctly.
# Create at least one object.
# Call all methods.
# show_result() should print PASS/FAIL.
# update_marks() should modify the marks.
class Student:
    def __init__(self,student_id,name,age,marks):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.marks=marks
    def study(self):
        print(f"{self.name} is studying")

    def take_exam(self):
        print(f"{self.name} is taking exam")
    def show_result(self):
        if self.marks>=250:
            print("PASS")
        else:
            print("FAIL")



    def show_profile(self):
        print(f"Student {self.name}, age {self.age} with student id: {self.student_id} has achieved marks: {self.marks}")

    def update_marks(self,grace):
        self.marks+=grace
        print(f"Updated marks: {self.marks}")
        
    

student_id=int(input("Enter id: "))
name=input("Enter name: ")
age=int(input("Enter your age: "))
marks=float(input("Enter marks: "))
obj=Student(student_id,name, age, marks)
obj.study()
obj.take_exam()
obj.show_result()
obj.show_profile()
obj.update_marks(15)

