# 
# Write a Python program that accepts 10 integers from the user and stores them in a list.
# Print the following:
# Original List
# First element
# Last element
# First 5 elements
# Last 5 elements
# Maximum number
# Minimum number
# Sum of all numbers
# Average
# Sort the list in ascending order.
# Sort the list in descending order.
# Reverse the list.
# Count how many times the number 10 appears.
# Find the index of 10 (if present).
# Remove the first occurrence of 10.
# Create a copy of the list and prove that modifying the copy does not affect the original list.
# Sample Input
# 10
# 20
# 30
# 10
# 40
# 50
# 60
# 70
# 80
# 90
# Sample Output
# Original : [10, 20, 30, 10, 40, 50, 60, 70, 80, 90]
# First : 10
# Last : 90
# First 5 : [10, 20, 30, 10, 40]
# Last 5 : [50, 60, 70, 80, 90]
# Maximum : 90
# Minimum : 10
# Sum : 460
# Average : 46.0
# Occurrences of 10 : 2
# Index of 10 : 0
import copy
l=[]
for i in range(10):
    item=int(input())
    l.append(item)
print(f"Original : {l}")
print(f"First : {l[0]}")
print(f"Last : {l[-1]}")
print(f"First 5 : {l[0:5]}")
print(f"Last 5 : {l[-5::]}")
print(f"Maximum : {max(l)}")
print(f"Minimum : {min(l)}")
print(f"Sum : {sum(l)}")
print(f"Average : {sum(l)/len(l)}")
print(f"Occurrences of 10 : {l.count(10)}")
print(f"Index of 10 : {l.index(10)}")
nl=copy.deepcopy(l)
nl[0]="Arya"
print(l)
