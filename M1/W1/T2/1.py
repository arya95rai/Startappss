# Print factorial

num = int(input("Enter any number: "))
f = 1

if num < 0:
    print("Not Defined")

else:
    if num == 0:
        print("Factorial is = 1")

    else:
        for i in range(1, num + 1):
            f *= i

        print(f"Factorial is: {f}")