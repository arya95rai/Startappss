while True:
    age = int(input("Enter your age: "))

    if age >= 0:
        print("Age after 5 years:", age + 5)
        break
    else:
        print("Invalid age")

# while True:
#     age = int(input("Enter your age: "))

#     if age < 0:
#         print("Invalid age")
#         continue

#     print("Age after 5 years:", age + 5)
#     break