# Create a set of unique vowels from a given string.
string=input("Enter a string: ")
s={x for x in string if x.lower() in "aeiou"}
print(s)