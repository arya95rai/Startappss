# Question
# Write a Python program that:
# Takes employee name.
# Takes employee age.
# Takes employee salary.
# Checks whether the employee is eligible for a senior role.
# Age ≥ 30
# Salary ≥ 50000
# Print all details using an f-string.
# Sample Input
# Name: Arya
# Age: 24
# Salary: 65000
# Sample Output
# Employee Details
# -----------------
# Name : Arya
# Age : 24
# Salary : 65000.0
# Eligible for Senior Role : False

name=input("Name: ")
age=int(input("Age: "))
salary=float(input("Salary: "))

print("Employee Details")
print("-----------------")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Salary : {salary}")
if age>=30:
    if salary>=50000:
        print(f"Eligible for Senior Role : True")

else:
    print(f"Eligible for Senior Role : False")
