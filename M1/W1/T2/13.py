#Find the largest number from 5 user inputs.
print("Enter 5 numbers: ")
largest=float(input())
for i in range(4):
    num=float(input())
    if num>largest:
        largest=num
print("Largest number among 5 entered is: ",largest)