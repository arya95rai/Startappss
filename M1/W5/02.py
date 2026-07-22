
# 2.
# Find the most common word in a paragraph using Counter.
from collections import Counter
para=input("Enter a paragraph: ").split()
p=Counter(para)
print(p.most_common(1))
