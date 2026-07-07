# Question

# Write a Python program that repeatedly asks the user to enter a number.

# Rules:

# If the number is negative, stop the program.
# If the number is 0, ignore it using continue.
# If the number is 100, do nothing using pass.
# Otherwise, add the number to the total.
# Count how many valid numbers were entered.

# When the loop ends, print:

# Total
# Count
# Average

# Use a while loop.

# Also use the else block of the loop to print:

# Loop ended successfully.

# (Note: The else block runs only if the loop is not terminated using break.)

# Sample Input
# 10
# 20
# 0
# 100
# 30
# -1
# Sample Output
# Total : 160
# Count : 4
# Average : 40.0
# Concepts Covered
# while
# break
# continue
# pass
# loop else
# nested if
# arithmetic operators
while True:
    flag=1
    total=0
    valid=0
    num=float(input())
    if num<0:
        flag=0
        break
    elif num==0:
        continue
    elif num==100:
        pass
    total+=num
    if num>0:
        valid+=1
print(f"Total : {total}")
print(f"Count : {valid}")
if valid!=0:
    print(f"Average : {total/valid}")
else:
    print(f"Average : 0")

if flag==1:
    print("Loop ended successfully.")




   
        
    








   
        

