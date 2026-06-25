#Take a sentence and count the total number of words
sentence=input("Enter a sentence: ")
s=sentence.split()
cnt=0
for i in s:
    cnt+=1
print(f"Total number of words: {cnt}")
