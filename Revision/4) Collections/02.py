# Write a Python program that accepts 8 integers from the user.
# Perform the following operations:
# Part A – Tuple
# Convert the list into a tuple.
# Print the tuple.
# Count how many times the number 5 appears.
# Find the index of 5 (if present).
# Demonstrate packing.
# Demonstrate unpacking.
# Create a single-element tuple.
# Part B – Set
# Convert the tuple into a set and print:
# Original Set
# Add the number 100.
# Update the set with {200, 300}.
# Remove 100.
# Discard 500.
# Pop one element.
# Create another set:
# {10,20,30,100,200}
# Print:
# Union
# Intersection
# Difference
# Whether the first set is a subset of the second.
# Whether the second set is a superset of the first.
print("Enter 8 integers: ")
l=[]
for i in range(8):
    item=int(input())
    l.append(item)
t=list(l)
print(t)
print(f"Number 5 appears: {t.count(5)} times")
print(f"Index of 5: {t.index(5)}")
#packing means converting integers, floating numvers etx into tuple
#unpacking is vice versa of packing
tup=(1,)
s=set(t)
print(s)
s.add(100)
s.update(200,300)
s.remove(100)
s.discard(500)
s.pop()
se={10,20,30,100,200}
print(s.union(se))
print(s.intersection(se))
print(s-se)
print(s.issubset(se))
print(se.issuperset(s))



