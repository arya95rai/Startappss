# Take a string from the user and count:
# Alphabets 
# Digits 
# Special Characters 
# Example:
# Input: Python123@
# Output:
# Alphabets = 6
# Digits = 3
# Special Characters = 1
string=input("Enter a string: ")
a_cnt=0
d_cnt=0
sc_cnt=0
for i in string:
    if i.isalpha()==True:
        a_cnt+=1
    elif i.isdigit()==True:
        d_cnt+=1
    else:
        sc_cnt+=1
print(f"Alphabet = {a_cnt}")
print(f"Digits = {d_cnt}")
print(f"Special Characters = {sc_cnt}")
