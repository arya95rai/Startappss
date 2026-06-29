# Find common elements between two sets.
s1=set()
s2=set()
n1=int(input("Enter the limit of first set: "))
n2=int(input("Enter the limit of second set: "))
for i in range(n1):
    item=input(f"Enter the element no {i+1}: ")
    s1.add(item)
for j in range(n2):
    ele=input(f"Enter the element no {j+1}: ")
    s2.add(ele)
print(s1 & s2)