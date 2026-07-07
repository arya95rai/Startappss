# Without using any temporary variable,

# Swap two numbers.
# Print memory address before swapping.
# Print memory address after swapping.
# Explain why memory address changes.
# Sample Input
# a = 100
# b = 200
# Expected Output
# Before Swap

# a = 100
# b = 200

# id(a) = 23456789
# id(b) = 98765432

# After Swap

# a = 200
# b = 100

# id(a) = 98765432
# id(b) = 23456789
print("Befor Swap")
print()
a=int(input("a = "))
b=int(input("b = "))
print()
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print()
print("After Swap")

a,b=b,a
print()
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")