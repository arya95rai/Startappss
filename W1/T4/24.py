# Take a string and check whether it contains only digits.
# Example:
# Input: 12345
# Output: Valid Number

string=input("Enter any string: ")
for i in string:
    if i.isdigit()==False:
        print("Invalid Number")
        break
else:
    print("Valid Number")
    

