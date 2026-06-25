#Take a string and check whether it starts with a given character.
string=input("Enter a string: ")
target=input("Enter the target element: ")
if string[0]==target:
    print(f"Yes it starts with: {target}")
else:
    print(f"No it doesnt start with {target}")
# string = input("Enter a string: ")
# target = input("Enter the target element: ")

# if string.startswith(target):
#     print(f"Yes, it starts with: {target}")
# else:
#     print(f"No, it doesn't start with: {target}")