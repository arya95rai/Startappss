#  Calculate average marks.
d={}
n=int(input("Enter limit of the dictionary: "))
for i in range(n):
    k=input(f"Enter subject no {i+1}: ")
    v=float(input("Enter marks of this subject: "))
    d[k]=v
print((sum(d.values())/len(d)))