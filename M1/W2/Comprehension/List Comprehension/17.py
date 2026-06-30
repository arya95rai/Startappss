
# Given a list of transaction IDs from 1 to 20, 
# create a new list where:

# Even IDs are labeled "Even"
# Odd IDs are labeled "Odd"

l=[x for x in range(1,21)]
nl=["Even" if i%2==0 else "odd" for i in range(1,21)]
print(nl)
