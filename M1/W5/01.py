# 1.
# Write a program to count the frequency of each character in a string using Counter.
# Example:
# Input:
# "banana"

# Output:
# {'b':1,'a':3,'n':2}\
from collections import Counter
s=input("Enter any string: ")
print(Counter(s))
