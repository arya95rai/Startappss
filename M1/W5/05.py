
# 5.
# Count how many employees belong to each department using defaultdict.
from collections import defaultdict
l=[
 ("Rahul","IT"),
 ("Aman","HR"),
 ("Rohit","IT")
 ]

d=defaultdict(int)
for name,dept in l:
    d[dept]+=1
print(dict(d))
