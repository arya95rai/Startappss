#Take a string and count how many uppercase letters and lowercase letters it contains
string=input("Enter any string: ")
uc=0
lc=0
for i in string:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
   
print(f"Total uppercase letter: {uc}")
print(f"Total lowercase letter: {lc}")