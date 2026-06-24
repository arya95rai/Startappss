l = []

limit = int(input("Enter limit of the list: "))

for i in range(limit):
    item = float(input(f"Enter element {i+1}: "))
    l.append(item)

target = float(input("Enter the number you want to find: "))

for i in l:
    if i == target:
        print(f"YES! The list has {target} in it")
        break
else:
    print("Number not found!")