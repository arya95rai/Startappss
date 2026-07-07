# Write a Python program that takes the marks of a student in 5 subjects.
# Print:
# Total Marks
# Percentage
# Grade according to the following:
# Percentage	Grade
# ≥ 90	A
# ≥ 80	B
# ≥ 70	C
# ≥ 60	D
# < 60	F
# Also print whether the student has Passed or Failed.
# A student passes only if:
# Percentage is at least 40
# No individual subject has marks less than 35
# Use:
# if
# elif
# else
# At least one nested if
# Print Pass/Fail using the ternary operator
# Sample Input
# 90
# 85
# 70
# 95
# 80
# Sample Output
# Total : 420
# Percentage : 84.0
# Grade : B
# Result : Pass
s1=float(input())
s2=float(input())
s3=float(input())
s4=float(input())
s5=float(input())
total=s1+s2+s3+s4+s5
percentage=(total/500)*100
print(f"Total : {total}")
print(f"Percentage : {percentage}")

if percentage>=90:
    print("Grade : A")
elif percentage>=80:
    print("Grade : B")
elif percentage>=70:
    print("Grade : C")
elif percentage>=60:
    print("Grade : D")
elif percentage<60:
    print("Grade : F")
else:
    print("Invalid input")
if percentage>=40:
    if (s1 and s2 and s3 and s4 and s5)>=35:
        result="Pass" if True else "Fail"
        print(f"Result : {result}")


    
