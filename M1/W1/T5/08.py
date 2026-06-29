#Find topper subject
d={}
n=int(input("Enter limit of the dictionary: "))
for i in range(n):
    k=input(f"Enter subject no: {i+1}: ")
    v=float(input(f"Enter marks of this subject: "))
    d[k]=v
for i in d:
    if d[i]==max(d.values()):
            print(f"{i} : {d[i]}") 