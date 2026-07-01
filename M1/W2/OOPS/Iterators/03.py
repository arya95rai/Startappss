# 3. Write a custom iterator that returns only odd numbers between 1 and 20.
class Odd:
    def __init__(self,start,end):
       self.current=start
       self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        while self.current<=self.end:
            if self.current%2!=0:
                value=self.current
                self.current+=1
                return value
            else:
                self.current+=1
                continue
        else:
            raise StopIteration()
obj=Odd(1,20)
for i in obj:
    print(i)