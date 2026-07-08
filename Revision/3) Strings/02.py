# Write a Python program that accepts a sentence from the user.
# Print:
# First character
# Last character
# First 5 characters
# Last 5 characters
# Reverse the sentence using slicing.
# Count how many times the letter 'a' appears.
# Find the first occurrence of the word "Python".
# Replace every occurrence of "Python" with "Java".
# Print every character on a new line using traversal.
# Print only the characters at even indexes.
# Sample Input
# I love Python because Python is simple
# Sample Output
# First Character : I
# Last Character : e
# First 5 : I lov
# Last 5 : imple
# Reverse : elpmis si nohtyP esuaceb nohtyP evol I
# Count of a : 0
# Python found at : 7
# After Replace : I love Java because Java is simple
sen=input()

s=sen.strip()
print(f"First Character: {sen[0]}")
print(f"Last Character : {s[0]}")
print(f"First 5 : {s[0:5]}")

print(s[len(s)-1:len(s)-6:-1])
print(s[::-1])
print(s.count('a'))
print(s.find('Python'))
print(s.replace('Python','Java'))
print(s.replace(" ","\n"))
print(s[0:len(s):2])
