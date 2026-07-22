# Create a descriptor that validates a student's age.
# ### Requirements
# * Create a descriptor named AgeDescriptor.
# * Age must be an integer.
# * Age cannot be negative.
# * If invalid, raise a ValueError.
# * Otherwise, store the value.
# ### Example
# python
# s = Student()
# s.age = 21
# print(s.age)
# s.age = -5
# Output
# 21
# ValueError
class AgeDescriptor:
    def __set__(self,instance,value):
        if value>0 and type(value)==int:

            instance.__dict__["age"]=value
        else:
            raise ValueError("Invalid Input")
    def __get__(self,instance,owner):
        return instance.__dict__["age"]
class Student():
    age=AgeDescriptor()
obj=Student()
obj.age=23
print(obj.age)
        
        

