#Print Fibonacci series up to N terms.
a=0
b=1
n=int(input("Enter the limit: "))
if n<=0:
    print("Invalid input")
else:
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
    