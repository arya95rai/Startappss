# Create a tuple of 10 numbers and 
# count how many numbers are greater than 50.
# Example:
# numbers = (10, 70, 20, 80, 30)
# Output:
# 2
t=()
cnt=0
print("Enter 10 numbers: ")
for i in range(10):
    item=float(input())
    t=t+(item,)
for i in t:
    if i>50:
        cnt+=1
print(cnt)

