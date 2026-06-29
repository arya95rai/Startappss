balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")