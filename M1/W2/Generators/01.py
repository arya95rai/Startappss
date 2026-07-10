# Write a generator that yields numbers from 1 to N.
def gen(n):
    for i in range(1,n+1):
        yield i
N=int(input("Enter limit: "))
for i in gen(N):
    print(i)