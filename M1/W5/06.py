# 6.
# Implement Stack using deque.
# Methods
# push()
# pop()
# peek()
# is_empty()
from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        else:
            return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return "Stack is empty"
        else:
            
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def display(self):
        print(self.stack)
            
s=Stack()
s.push("Arya")
s.display()
s.push("Pehu")
s.display()
s.push("Ayan")
s.display()

s.pop()
print(s.pop())
s.display()

print(s.peek())
print(s.is_empty())
    

      

