# Create custom AgeValidationError
class AgeValidationError(Exception):
    pass
try:
    age=int(input("Enter your age: "))
    if age<18:
        raise AgeValidationError("Age must be atleast 18!")
   
except ValueError:
    print("Please enter a valid integer")
except AgeValidationError as e:
    print(e)
else:
    print("Age accepted")





