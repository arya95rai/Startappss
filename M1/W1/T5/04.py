# Count vowels using a set.
string=input("Enter a string: ")
v={'a','e','i','o','u'}
cnt=0
for i in string:
    if i.lower() in v:
        cnt+=1
print(cnt)