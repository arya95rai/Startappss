# Login System (3 Attempts)

# Rules:

# Correct username and password
# Maximum 3 attempts
# Lock account after 3 failures
name="Arya"
p="arya7"
for i in range(3):
    uname=input("Enter your name: ")
    password=input("Enter password: ")
    if uname==name and password==p:
        print(f"Welcome {uname}!")
        break
    else:
        print("Try again ")
else:
    print("OOPS! System locked")
    