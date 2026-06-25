# Count frequency of words in a sentence.
sen=input("Enter any sentence: ")
d={}
sen=sen.split()
for i in sen:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
    