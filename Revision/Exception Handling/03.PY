# Write a program that simulates an ATM withdrawal.
# Requirements:
# Ask the user to enter the account balance.
# Ask the user to enter the withdrawal amount.
# If the user enters invalid input, display an appropriate error message.
# If the withdrawal amount is greater than the balance, display:
# Insufficient balance
# Otherwise, display the remaining balance.
# Regardless of whether the transaction succeeds or fails, display:
# Thank you for using our ATM.
try:
    balance=float(input("Enter account balance: "))
    amount=float(input("Enter withdrawl amount: "))
    remaining_balance=balance-amount
    if amount>balance:
        print("Insufficient balance")
    else:
        print(remaining_balance)
except ValueError:
    print("Invalid input")
finally:
    print("Thank you for using our ATM.")