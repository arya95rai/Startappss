# Write a program that asks the user to enter their age.

# Requirements:

# If the input is not a valid integer, display an error message.

# Otherwise, display:

# Age accepted: <age>
# The program should continue normally without crashing.
try:
    age=int(input("Enter age: "))
except ValueError:
    print("Age can only be positive integers")
else:
    print(f"Age accepted: {age}")