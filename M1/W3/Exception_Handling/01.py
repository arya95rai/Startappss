#handle division by zero and invalid input
try:
    num=float(input("Enter a number: "))
    result=100/num

except ZeroDivisionError as e:
    print("Cannot divide by 0",e)
except ValueError as e:
    print("Invalid input",e)
else:
    print(result)

    