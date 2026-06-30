# Create a list of common elements between two lists.
n1=int(input("Enter the limit of list 1: "))
n2=int(input("Enter the limit of list 1: "))
l1=[input(f"Enter element no {i+1}") for i in range(n1)]
l2=[input(f"Enter element no {i+1}") for i in range(n2)]
common=[x for x in l1 if x in l2]
print(common)

