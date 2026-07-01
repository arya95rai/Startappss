# 9. Create an infinite iterator that generates consecutive integers starting from 1.
# Example:

# obj = Counter()
# for _ in range(10):
#     print(next(obj))
class Counter():
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        
            value=self.num
            self.num+=1
            return value
       
obj=Counter()
for _ in range(10):
    print(next(obj))

      
