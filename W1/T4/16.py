# Create a list with duplicate values and remove duplicates 
# without using set().
# Example:
# Input: [1,2,2,3,4,4,5]

# Output: [1,2,3,4,5]
l=[]
n=int(input("Enter limit of the list: "))
for i in range(n):
    item=input(f"Enter element no {i+1}: ")
    l.append(item)
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print(unique)