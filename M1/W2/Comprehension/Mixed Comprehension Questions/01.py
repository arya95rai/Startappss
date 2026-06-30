# Find frequency of each element 
# in a list using dictionary comprehension
n=int(input("Enter limit of the list: "))
l=[input(f"Enter element no {i+1}: ") for i in range(n)]
d={
    k:l.count(k) for k in l
}
print(d)


    


