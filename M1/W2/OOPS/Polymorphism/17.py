# 17.	Write a program that demonstrates duck typing using 
# different classes having the same display() method.
class Tv:
    def display(self):
        print("TV display")

class Phone:
    def display(self):
        print("Phone display")
def Dis(obj):
    obj.display()
t=Tv()
p=Phone()
Dis(t)
Dis(p)
