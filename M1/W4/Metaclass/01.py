# 1. Create a metaclass that converts every 
# class attribute name to uppercase during class creation.
# Example
# class Student(metaclass=MyMeta):
#     name = "Rahul"
# Should become internally:
# NAME = "Rahul"
class MyMeta(type):
    def __new__(cls,name,bases,attrs):
        new_attrs={}
        for k,v in attrs.items():
            if k.startswith("__"):
                new_attrs[k]=v
            else: 
                new_attrs[k.upper()]=v
        return super().__new__(cls,name,bases,new_attrs)
    
    
        
class test(metaclass=MyMeta):
    name = "Rahul"
print(test.__dict__)
print(test.NAME)

    
    
