# Given:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Create a list containing 
# all elements of the matrix in a single list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
l=[j for i in matrix for j in i]
print(l)
