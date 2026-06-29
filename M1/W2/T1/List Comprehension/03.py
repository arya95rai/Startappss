# Create a list containing the length of each word in:
# words = ["python", "java", "c++", "javascript"]
words = ["python", "java", "c++", "javascript"]
l=[]
# for i in words:
#     l.append(len(i))
l=[len(i) for i in words]
print(l)