# #Take a string and find the longest word.
# Example:
# Input: Python is very easy to learn

# Output: Python
string=input("Enter any string: ")
l=string.split()
max=l[0]
for i in l:
    if len(i)>len(max):
        max=i
print(max)