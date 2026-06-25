# Take 5 names in a list and print them in alphabetical order.
# Example:
# Input:
# ["Ram", "demo", "Mohan"]
# Output:
# ["demo", "Mohan", "Ram"]
l=[]
for i in range(5):
    item=input(f"Enter name {i+1}: ")
    l.append(item)
l.sort()
print(l)