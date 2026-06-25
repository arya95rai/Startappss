# Create a tuple of 10 numbers and find:
# Maximum number
# Minimum number
# Sum of all numbers
t=[]
for i in range(10):
    item=float(input(f"Enter element no {i+1}: "))
    t.append(item)
t=tuple(t)
print(max(t))
print(min(t))
print(sum(t))
