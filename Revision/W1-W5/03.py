# "I have a list of employee names. 
# Some names appear multiple times because of duplicate records in our database.
# Write a program that removes the duplicates
#  without using a set, while preserving the original order of the names.
# Input:
# employees = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]
# Expected Output:
# ["Alice", "Bob", "Charlie", "David"]
# Constraint: Do not use set() or any built-in function 
# specifically meant for removing duplicates.
employees = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]
unique=[]
for employee in employees:
    if employee not in unique:
        unique.append(employee)
print(unique)



        

        
        
