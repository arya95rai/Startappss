# Take a string and create a new string 
# containing only the even index characters.
# Example:
# Input: Python
# Output: Pto
string=input("Enter a string: ")
new_str=""
for i in range(0,len(string),2):
    new_str+=string[i]
print(new_str)