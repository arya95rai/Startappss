# 13.	Create Developer, Tester, and Manager classes with a work() method. 
# Store all objects in a list and execute their methods using polymorphism.
class Developer:
    def work(self):
        print("I am a developer")
class Tester:
    def work(self):
        print("I am a tester")
class Manager:
    def work(self):
        print("I am a manager")
emp=[Developer(),Tester(),Manager()]
for i in emp:
    i.work()

