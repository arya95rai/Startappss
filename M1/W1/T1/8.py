 #Create a simple calculator using choice:
# 1 Addition
# 2 Subtraction
# 3 Multiplication
# 4 Division
print("Enter two numbers: ")
n1=float(input())
n2=float(input())
choice=input("Enter your choice from: add,sub,mul,div:  ")
if choice=="add":
    print(n1+n2)
elif choice== "sub":
    print(n1-n2)
elif choice=="mul":
    print(n1*n2)
elif choice=="div":
    print(n1/n2)
else:
    print("Invalid input")
    