# #Create a list of 10 numbers and create 
# a new list containing only numbers greater than 25.
# Example:
# Input: [10,20,30,40]
# Output: [30,40]
l=[]
print("Enter 10 numbes: ")
for i in range(10):
    item=float(input())
    l.append(item)
nl=[]
for i in l:
    if i>25:
        
        nl.append(i)

print(nl)
