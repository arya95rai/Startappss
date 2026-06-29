# Group students by grade using a dictionary
d={}
n=int(input("Enter the total number of students: "))
for i in range(n):
    k=input(f"Enter name of student no: {i+1}: ")
    v=input(f"Enter grade: ")
    d[k]=v
nd={}
for k,v in d.items():
    if v not in nd:
        nd[v]=[k]
    else:
        nd[v].append(k)
print(nd)


