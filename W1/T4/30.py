# Create a tuple of employee names and 
# check whether a given employee name exists in the tuple.
# Example:
# Input: demo
# Output:
# Employee Found
t=()
n=int(input("Enter the limit of tuple: "))
for i in range(n):
    item=input(f"Enter employee no (i+1): ")
    t=t+(item,)
target=input("Enter the name of employee you want to find: ")
for i in t:
    if i==target:
        print("Employee Found")
        break
else:
    print("Employee Not Found")
    
