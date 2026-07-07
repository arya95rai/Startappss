# Write a Python program that takes an integer N from the user and prints the following pattern.
# Sample Input
# 5
# Sample Output
# 1
# 12
# 123
# 1234
# 12345
# Now print the reverse pattern.
# 12345
# 1234
# 123
# 12
# 1
# Finally, print only the even numbers in the pattern.
# 2
# 24
# 246
# 2468
# 246810
# Restrictions:
# Use only for loops.
# Use range().
# Use nested loops.
# Use continue to skip odd numbers in the even-number pattern.
N=int(input())
print()
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print()
for i in range(N,0,-1):
    for j in range(1,N+1):
        print(j,end="")
    N-=1
    print()
print()
for i in range(1,N+1):
    for j in range(1,i+1):
        if j%2==0:
            print(j,end="")
    print()
print()
