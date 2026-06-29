# #Take 5 student names in a list and search 
# for a specific student name.
# If found print:
# Student Found
# otherwise:
# Student Not Found
l=[]
for i in range(5):
    item=input(f"Enter student {i+1}: ")
    l.append(item)
target=input("Enter the student you need to find: ")
for i in l:
    if i==target:
        print("Student Found")
        break
else:
    print("Student Not Found")

