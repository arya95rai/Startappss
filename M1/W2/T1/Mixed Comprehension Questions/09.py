# Create a list of prime numbers between 1 and 100 using list comprehension.

l=[n for n in range(2,101) if all(n%i !=0 for i in range(2,n))]
print(l)