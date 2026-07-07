# 2. Student Management System
# Create a Student class.
# Attributes (8)
# •	student_id
# •	name
# •	age
# •	gender
# •	class_name
# •	section
# •	roll_number
# •	marks
# Methods (5)
# •	study()
# •	attend_class()
# •	take_exam()
# •	show_result()
# •	show_profile()
class Student:
    def __init__(self,student_id,name,age,gender,class_name,section,roll_number,marks):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.gender=gender
        self.class_name=class_name
        self.section=section
        self.roll_number=roll_number
        self.marks=marks
    def study(self):
        print(f"Student {self.name} is studying")
    def attend_class(self):
        print(f"Student {self.name} is attending {self.class_name}")
    def take_exam(self):
        print(f"Student {self.name} with roll no: {self.roll_number} is taking exam")
    def show_result(self):
        if self.marks>=250:
            print(f"PASS")
        else:
            print("FAIL")
        
    def show_profile(self):
        print(f"Student {self.name} has {(self.marks/500)*100}%")

obj=Student()

