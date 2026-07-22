# 3.
# Print the top 5 most frequent numbers from a list.
from collections import Counter
l=[1,2,1,1,1,3,4,5,6,6,6,6,6,7,8]
print(Counter(l).most_common(5))
