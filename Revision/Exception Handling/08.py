# Write a program that:
# Takes an integer as input.
# If the user enters invalid data:
# Catch the ValueError.
# Raise a new Exception("Invalid input provided") using exception chaining.
try:
    n=int(input("Enter a number: "))
except ValueError as e:
    raise ValueError("Invalid input provided") from e
else:
    print(f"The number is: {n}")
    
