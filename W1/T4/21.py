# Take a string and find the first non-repeated character.
# Example:
# Input: swiss
# Output:
# w

string=input("Enter a string: ")
d={}
for i in string:
    d[i]=d.get(i,0)+1
for i in d:
    if d[i]==1:
        print(i)
        break