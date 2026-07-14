# Take two numbers as input.
# If division by zero occurs:

# Print "Logging error..."
# Re-raise the exception.
try:
    n=float(input("Enter 1st no: "))
    d=float(input("Enter 2nd no: "))
    result=n/d
except ZeroDivisionError:
    print("Logging error...")
    raise
