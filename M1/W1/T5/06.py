#  Calculate total marks from a dictionary.
d={}
n=int(input("Enter limit of the dictionary: "))
for i in range(n):
    k=input("Enter subject no {i+1}: ")
    v=float(input("Enter marks of this subject: "))
    d[k]=v
print(f"Total marks: {sum(d.values())}")
