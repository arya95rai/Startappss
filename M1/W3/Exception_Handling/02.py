#Create custom AgeValidationError
class AgeValidationError(Exception):
    pass
try:
    age=int(input("Enter age: "))
except ValueError as e:
    if age<18:
        raise AgeValidationError("Invalid age") from e
except Exception as e:
    print(e)
else:
    print("Valid age")
        
