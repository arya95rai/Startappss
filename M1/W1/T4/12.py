#  Take 5 marks from the user and store them in a list. Calculate:
# Total
# Average
# Highest Marks
# Lowest Marks
l=[]
for i in range(5):
    item=float(input(f"Enter subject {i+1} marks: "))
    l.append(item)
print(f"Total= {sum(l)}")
print(f"Average= {(sum(l)/5)}")
print(f"Highest marks= {max(l)}")
print(f"Highest marks= {min(l)}")