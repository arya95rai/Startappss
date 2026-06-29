# Create a table generator program.
# Enter Number: 7

# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
n=int(input("Enter any number: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")