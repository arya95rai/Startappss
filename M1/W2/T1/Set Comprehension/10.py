
# Create a set of common elements from two lists.
n1=int(input("Enter the limit of first list: "))
l1=[input(f"Enter element no {i+1}") for i in range(n1)]
n2=int(input("Enter the limit of second list: "))
l2=[input(f"Enter element no {i+1}") for i in range(n2)]
s={x for x in set(l1) & set(l2)}
print(s)
