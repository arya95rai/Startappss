#Find the sum of digits of a number.
n=int(input("Enter any number: "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)