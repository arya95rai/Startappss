# #Check login eligibility:
# Username = admin
# Password = 1234
username=input("Enter your username: ")
password=int(input("Enter your password: "))
if username=="admin" and password==1234:
    print("Logged in")
else:
    print("Invalid credentials")