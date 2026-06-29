
# Create a dictionary mapping numbers 
# from 1 to 10 to "Even" or "Odd".
d={
    i:"Even" if i%2==0 else "Odd" for i in range(1,11)
}
print(d)