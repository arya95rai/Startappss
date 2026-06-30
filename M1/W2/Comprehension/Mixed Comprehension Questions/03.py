# Flatten a nested list and store only unique values using set comprehension.
r=int(input("Enter no of rows: "))
c=int(input("Enter no of columns: "))
matrix=[]
for i in range(r):
    rows=[]
    for j in range(c):
        item=input(f"Enter element no {i}{j}: ")
        rows.append(item)
    matrix.append(rows)

l=[j for i in matrix for j in i]
print(set(l))

# r = int(input("Enter rows: "))
# c = int(input("Enter columns: "))

# matrix = []

# for i in range(r):
#     row = input(f"Enter row {i+1}: ").split()
#     matrix.append(row)

# unique = {j for i in matrix for j in i}

# print(unique)
    