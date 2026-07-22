# 4.
# Group students department-wise using defaultdict.
# Input
# [
# ("Rahul","IT"),
# ("Aman","HR"),
# ("Rohit","IT")
# ]
from collections import defaultdict
d=defaultdict(list)
l=[
 ("Rahul","IT"),
 ("Aman","HR"),
 ("Rohit","IT")
 ]
for name, dept in l:
    d[dept].append(name)

print(d)

