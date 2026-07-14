# Handle division by zero and invalid input
try:
    n=float(input("Enter numerator: "))
    d=float(input("Enter denominatior: "))
    n/d
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid Input")