# Create all possible pairs from:

# list1 = [1, 2, 3]
# list2 = ['A', 'B']
list1 = [1, 2, 3]
list2 = ['A', 'B']
l=[(i,j) for i in list1 for j in list2]
print(l)