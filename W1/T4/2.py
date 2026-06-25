#Take a string and count how many vowels (a, e, i, o, u) are present.
string=input("Enter any string: ")
cnt=0
for i in string:
    if i in "aeiouAEIOU":
        cnt+=1

print(f"Number of vowels: {cnt}")