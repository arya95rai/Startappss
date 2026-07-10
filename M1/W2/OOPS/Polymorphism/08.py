# 18.	Create a Shape hierarchy with an area() method in each child class 
# and write a function that accepts any shape object to calculate/display its area.
class Square:
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)


    
class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
    
def shape(obj):
    obj.area()
side=float(input("Enter side of square: "))
s=Square(side)
len=float(input("Enter length of rectangle: "))
bre=float(input("Enter breadth of rectangle: "))
r=Rectangle(len,bre)
shape(s)
shape(r)


        


