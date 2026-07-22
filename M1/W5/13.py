# 13.
# Find the first unique character.
# apple
# ↓
# Output
# a
from collections import Counter
word=input("Enter any word: ")
c=Counter(word)
for k,v in c.items():
    if v==1:
        print(k)
        break