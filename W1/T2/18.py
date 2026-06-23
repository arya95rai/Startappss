# Print even numbers using while loop
i=0
limit=int(input("Enter the limit: "))
while i<=limit:
    if i%2==0:
        print(i)
    i+=1