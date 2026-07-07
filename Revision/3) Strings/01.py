# Write a Python program that takes a full name from the user.
# Print the following:
# Original Name
# Name in Uppercase
# Name in Lowercase
# Name in Title Case
# Name in Capitalized form
# Swap the case of every letter.
# Remove extra spaces from both ends.
# Total number of characters (excluding leading/trailing spaces).
# Whether the name starts with 'A'.
# Whether the name ends with 'a'.
# Use:
# Indexing
# strip()
# upper()
# lower()
# title()
# capitalize()
# swapcase()
# startswith()
# endswith()
# len()
# Sample Input
#    arya rai
# Sample Output
# Original :    arya rai
# Upper : ARYA RAI
# Lower : arya rai
# Title : Arya Rai
# Capitalize : Arya rai
# Swapcase : ARYA RAI
# Trimmed : arya rai
# Length : 8
# Starts with A : False
# Ends with a : False
name=input()
full_name=name.strip()
print(f"Original : {name}")
print(f"Upper : {full_name.upper()}")
print(f"Lower : {full_name.lower()}")
print(f"Title : {full_name.title()}")
print(f"Cpitalize : {full_name.capitalize()}")
print(f"Swapcase : {full_name.swapcase()}")
print(f"Trimmed : {full_name.strip()}")
print(f"Length : {len(full_name)}")#i dont get it why every other syntax is same but for len we write len(strname) and not strname.len()
print(f"Starts with A : {full_name.startswith('A')}")
print(f"Ends with a : {full_name.endswith('a')}")