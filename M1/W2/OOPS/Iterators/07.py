# 7. Create your own implementation of Python's range(start, stop) using an iterator class.
# Example:

# obj = MyRange(5, 10)
# for i in obj:
#     print(i)
class MyRange:
    def __init__(self,start,end):
        self.current=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.end:
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration("--End--")
obj=MyRange(5,10)
for i in obj:
    print(i)
        
    
    