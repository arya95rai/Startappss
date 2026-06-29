# Remove duplicates from a list using set.
l=[]
n=int(input("Enter the maximum no of elements: "))
for i in range(n):
    item=input(f"Enter element no {i+1}: ")
    l.append(item)
s=set(l)
nl=list(s)
print(nl)