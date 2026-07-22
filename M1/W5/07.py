# 7.
# Implement Queue using deque.
# Methods
# enqueue()
# dequeue()
# front()
# rear()
from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue)==0:
            return "Queue is empty"
        else:
            return self.queue.popleft()
    def front(self):
        if len(self.queue)==0:
            return "Queue is empty"
        else:
            return self.queue[0]
    def rear(self):
        if len(self.queue)==0:
            return "Queue is empty"
        else:
            return self.queue[-1]
q=Queue()
q.enqueue("arya")
q.enqueue("pehu")
q.enqueue("ayan")
print(f"This was dequeued: {q.dequeue()}")
print(q.front())
print(q.rear())
