# Create a list of 10 numbers and count how many 
# numbers are even and odd
l=[]
for i in range(10):
    item=int(input(f"Enter element no {i+1}: "))
    l.append(item)
cnt_eve=0
cnt_odd=0
for i in l:
    if i%2==0:
        cnt_eve+=1
    elif i%2!=0:
        cnt_odd+=1
print(f"No of even elements= {cnt_eve}")
print(f"No of odd elements= {cnt_odd}")




