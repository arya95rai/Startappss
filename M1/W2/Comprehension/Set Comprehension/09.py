# Create a set containing only uppercase letters from a string.
string=input("Enter any string: ")
s={x for x in string if x==x.upper()}
print(s)