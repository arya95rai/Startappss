# 🏦 Problem Statement

# You are asked to design a simple Bank Account system for a fintech application.

# 🔒 Requirements:

# Create a class BankAccount with:

# Private Attribute:
# __balance
# ⚙️ Methods:
# deposit(amount)
# Add money to the account
# Only allow positive amounts
# If invalid, print "Invalid deposit amount"
# withdraw(amount)
# Allow withdrawal only if sufficient balance exists
# If amount is greater than balance, print "Insufficient balance"
# get_balance()
# Return the current balance
# 📌 Constraints:
# Balance must never be accessed directly from outside the class
# All updates must go through methods only (encapsulation required)
# 🧾 Input/Output Behavior (Example Flow):
# Account created with balance = 1000

# deposit(500)
# withdraw(200)
# withdraw(2000)

# Output:
# Invalid withdrawal: Insufficient balance

# Final Balance = 1300
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Balance after withdrawal: {self.__balance}")
        else:
            print("Invalid withdrawal: Insufficient balance")

    def get_balance(self):
        return self.__balance


balance = float(input("Account created with balance = "))
obj = BankAccount(balance)

obj.deposit(500)
obj.withdraw(200)
obj.withdraw(2000)

print("Final Balance =", obj.get_balance())
