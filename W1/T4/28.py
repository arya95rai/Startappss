# Create two lists:
# list1 = [10, 20, 30]
# list2 = [40, 50, 60]
# Merge them into a single list.
# Output:
# [10, 20, 30, 40, 50, 60]
l1=[]
n1=(int(input("Enter limit of first list: ")))
for i in range(n1):
    item=input(f"Enter item {i+1}:")
    l1.append(item)
l2=[]
n2=int(input("Enter limit of second list: "))
for i in range(n2):
    item=input(f"Enter item {i+1}:")
    l2.append(item)
print(l1+l2)
   
