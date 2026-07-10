# Write a program that acts as a simple calculator.

# Requirements:

# Take two integers as input from the user.
# Divide the first number by the second.
# If the user enters invalid data, display an appropriate message.
# If the user attempts to divide by zero, display an appropriate message.
# If the operation succeeds, display the result.
# The program should not crash regardless of the input.
try:
    n1=int(input("Enter first integer: "))
    n2=int(input("Enter second integer: "))
    result=n1/n2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print(f"Result= {result}")

