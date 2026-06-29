# Create a lambda function that takes three numbers and returns the largest value among them.
m=lambda x,y,z : max(x,y,z)
x=float(input("Enter first no: "))
y=float(input("Enter second no: "))
z=float(input("Enter third no: "))
m(x,y,z)