# Design a BankAccount class with the following requirements:
# Attributes
# account_holder
# balance
# Methods
# deposit(amount) – Add money to the account.
# withdraw(amount) – Withdraw money if sufficient balance exists.
# check_balance() – Display the current balance.
# Requirements
# Use a constructor to initialize the account.
# Use instance variables (self).
# Prevent withdrawal if the balance is insufficient.
# Create an object and demonstrate all methods.
class BankAccount:
    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    # Check balance
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Create an object
account1 = BankAccount("Arya Rai", 5000)

# Demonstrate all methods
account1.check_balance()

account1.deposit(2000)
account1.check_balance()

account1.withdraw(3000)
account1.check_balance()

account1.withdraw(5000)  # Insufficient balance
