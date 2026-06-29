#  Find missing numbers from a set. 
s=set()
n=int(input("Enter limit of set: "))
for i in range(n):
    item=int(input("Enter sequence of numbers with a misssing number: "))
    s.add(item)
full_set=set(range(min(s),max(s)+1))
print(full_set-s)