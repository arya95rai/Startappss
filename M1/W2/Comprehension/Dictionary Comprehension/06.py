# Create a frequency dictionary of characters 
# in a string using dictionary comprehension.
s=input("Enter any string: ")
d={
    ch:s.count(ch) for ch in s
}
print(d)