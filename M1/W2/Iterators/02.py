# 2. Create a class NumberIterator that iterates over numbers from 1 to 10.
# Example:
# obj = NumberIterator()
# for i in obj:
#     print(i)
class NumberIterator:
    def __init__(self,start,end):
        self.current=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.end:
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration("--End--")
            
obj=NumberIterator(1,10)
for i in obj:
    print(i)

    
  
        

