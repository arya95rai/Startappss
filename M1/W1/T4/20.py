# Create a tuple of subject names and a list of marks. Print:
# Maths : 90
# English : 85
# Science : 80
# using a loop.
sub=()
marks=[]
n=int(input("Enter the no of subjects: "))
for i in range(n):
    s=input(f"Enter subject no {i+1}: ")
    m=float(input("Enter marks of this subject: "))
    sub=sub+(s,)
    marks.append(m)
for s,m in zip(sub,marks):
    print(f"{s} : {m}")
    
    