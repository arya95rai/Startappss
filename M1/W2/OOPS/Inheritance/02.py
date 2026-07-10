# 2.	Create a multilevel inheritance example 
# using Person → Employee → Manager. Add different methods at each level 
# and demonstrate method access.
class Person:
    def live(self):
        print("I am just a human")
class Employee(Person):
    def work(self):
        print("I work at a company")

class Manager(Employee):
    def tasks(self):
        print("I manage tasks")

obj=Manager()
obj.live()
obj.work()
obj.tasks()