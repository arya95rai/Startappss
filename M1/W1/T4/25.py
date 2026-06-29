# Create a list of 10 numbers and print the square of each number.
# Example:
# Input: [1,2,3]
# Output:
# 1
# 4
# 9
l=[]
for i in range(10):
    item=float(input("Enter 10 numbers: "))
    l.append(item)
for i in l:
    print(i**2)