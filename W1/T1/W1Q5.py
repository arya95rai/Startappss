# Check Greater Number

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if n1 > n2:
    print(f"{n1} is greater")
elif n2 > n1:
    print(f"{n2} is greater")
else:
    print("Both are equal")