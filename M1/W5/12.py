
# 12.
# Find duplicate words in a text using Counter.
from collections import Counter
text=input("Enter any text: ").split()
c=Counter(text)
print(c)
for k,v in c.items():
    if v>1:
        print(k)

    

