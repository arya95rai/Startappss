# Create a descriptor that stores a student's age and returns it when accessed.
class MyDescriptor:
    
    def __set__(self, instance, value):
        instance.__dict__["age"]=value
    def __get__(self, instance, owner):
        return instance.__dict__["age"]
    
    
class Age:
    age=MyDescriptor()
obj=Age()
obj.age=23
print(obj.age)

