# Write a Python program that accepts 5 numbers from the user.
# Then print:
# Original List
# Maximum value
# Minimum value
# Sum
# Average
# Whether number 50 exists in the list.
# Convert the list into:
# tuple
# set
# Sample Input
# 10
# 20
# 30
# 40
# 50
# Sample Output
# List : [10, 20, 30, 40, 50]
# Tuple : (10, 20, 30, 40, 50)
# Set : {10,20,30,40,50}
# Maximum : 50
# Minimum : 10
# Average : 30
# 50 exists : True
l=[]
for i in range(5):
    num=int(input())
    l.append(num)
print(f"List : {l}")
t=tuple(l)
print(f"Tuple : {t}")
s=set(t)
print(f"Set : {s}")
l=list(s)
print(f"Maximum : {max(l)}")
print(f"Minimum : {min(l)}")
print(f"Average : {sum(l)//len(l)}")
for i in l:
    if i==50:
        print("50 exists : True")




