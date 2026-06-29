# #Take a string and print the frequency of each character.
# Example:
# Input: banana
# Output:
# b = 1
# a = 3
# n = 2
string=input("Enter a string: ")
d={}
for i in string:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    print(f"{i}={d[i]}")


    
