age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Eligible for voting")
else:
    print("Ineligible for voting")
