# Create a generator that yields even numbers up to N.
def gen(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
N=int(input("Enter limit: "))
for i in gen(N):
    print(i)
