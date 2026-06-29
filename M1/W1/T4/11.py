# Create a list of 10 numbers and print all numbers greater than 50.
l=[]
print("Enter 10 elements: ")
for i in range(10):
    item=int(input(f"Enter element no {i+1}: "))
    l.append(item)
print("Elemetns greater than 50: ")
for i in l:
    if i>50:
        print(i)

