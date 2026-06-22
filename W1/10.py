# Check ATM withdrawal eligibility:
# Balance ≥ Amount
balance=float(input("Enter account balance: "))
amount=float(input("Enter withdrawal amount: "))
if balance>=amount:
    print("sufficient balance")
else:
    print("insufficient balance")