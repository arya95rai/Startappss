# Create a tuple containing:
# Name
# Age
# City
# Course
# Use tuple unpacking and print each value separately.
name=input("Enter name: ")
age=int(input("Enter age: "))
city=input("Enter city: ")
course=input("Enter course: ")
t=(name,age,city,course)
n,a,c,co=t
print(n)
print(a)
print(c)
print(co)