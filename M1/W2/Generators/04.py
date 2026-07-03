# # 1
# Write a generator for Fibonacci sequence up to N terms.

n=int(input("Enter limit of fibonacci: "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a
    a=b
    b=a+b
   