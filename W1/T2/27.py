##Check Armstrong number.
n=int(input("Enter a number: "))
temp=n
sum=0
while n>0:
    digit=n%10
    n=n//10
    sum=sum+(digit*digit*digit)
if temp==sum:
    print("Armstrong")
    
else:
    print("Not armstrong")
    
    
    
    