# 8.
# Create a namedtuple for Student.
# Fields
# id
# # name
# salary
# Print all students earning more than ₹50,000.
from collections import namedtuple
Student=namedtuple("Student",["id","name","salary"])
s=Student("a1","arya",50001)
s1=Student("a2","pehu",60000)
s2=Student("a3","ayan",34000)
l=[s,s1,s2]
for i in l:
    if i.salary>50000:
        print(i.name)

