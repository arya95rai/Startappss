#Create a list of numbers and print only odd numbers.
l=[]
n=int(input("Enter max no of elements in the list: "))
for i in range(n):
    item=int(input(f"Enter item no {i+1}: "))
    l.append(item)
for j in l:
    if j%2!=0:
        print(j)

    
        
    
             
                   