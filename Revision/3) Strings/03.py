# Wrong :(
# Write a Python program that takes a password from the user.
# Validate the password using the following rules:
# Length should be at least 8 characters.
# It should contain at least:
# one uppercase letter
# one lowercase letter
# one digit
# It should not contain spaces.
# If valid, print:
# Password Accepted
# ASCII value of every character.
# Unicode code point of every character using ord().
# Convert the password into a list using split() (use any suitable delimiter if needed).
# Join the list back into a string using join().
# Print the password centered in a field of width 20 using center().
# Print the password padded to length 12 using zfill().
# Otherwise print:
# Invalid Password
# Sample Input
# Python123
# Sample Output
# Password Accepted
# P -> ASCII : 80
# y -> ASCII : 121
# t -> ASCII : 116
# h -> ASCII : 104
# o -> ASCII : 111
# n -> ASCII : 110
# 1 -> ASCII : 49
# 2 -> ASCII : 50
# 3 -> ASCII : 51
# Joined : Python123
# Centered :      Python123
# Zfill : 000Python123
password=input()
if len(password)>=8 and password.isupper() and password.islower() and password.isdigit() and password.find(""):
    print("Password Accepted")
else:
    print("Invalid Password")
for i in password:
    print(ord(i))
l=password.split()
p=password.join(l)
print(f"Joinded : {p}")
print(f"Centered : {p.center(12)}")
print(f"Zfill : {p.zfill(12)}")


    
    
        

