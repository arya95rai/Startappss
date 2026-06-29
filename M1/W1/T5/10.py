# Create a contact book using a dictionary.
d={}
n=int(input("Enter the maximum no of contacts: "))
print(f"Enter names of {n} people: ")
for i in range(n):
    k=input()
    v=int(input("Enter contact no of this person: "))
    d[k]=v
print(f"Contact book: ")
for k,v in d.items():
    print(f"{k} : {v}")