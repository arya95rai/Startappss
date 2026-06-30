# 13. Bank Withdrawal System

# Given a balance of 10000, ask the user for a withdrawal amount.

# Raise a custom exception if the withdrawal amount exceeds the balance.
balance=10000
amount=float(input("Enter amount for withdrawal: "))
class LimitExceeded(Exception):
    pass
if balance<amount:
    raise LimitExceeded("Insufficient Balance")

