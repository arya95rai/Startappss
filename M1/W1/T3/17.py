# #Number Guessing Game

# Rules:

# Secret number = 25
# User gets 5 chances
# Show Higher/Lower hints

secret_no=25
for i in range(5):
    n=int(input("Enter any integer: "))
    if n==secret_no:
        print("You won!")
        break
    elif n<secret_no:
        print("Hint: Higher than this number")
    else:
        print("Hint: GO lower")
else:
    print("Game over!")