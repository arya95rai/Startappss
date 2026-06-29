balance = 50000
choice = int(input("Enter your choice: "))

if choice == 1:
    print(f"Available balance: Rs.{balance}")

elif choice == 2:
    amount = float(input("Enter amount: "))

    if balance >= amount:
        balance -= amount
        print("Withdrawal successful!")
        print(f"Remaining balance: Rs.{balance}")
    else:
        print("Insufficient balance")

elif choice == 3:
    deposit = float(input("Enter deposit amount: "))
    balance += deposit
    print(f"Rs.{deposit} deposited")
    print(f"Updated balance: Rs.{balance}")

elif choice == 4:
    print("Exited")

else:
    print("Invalid choice")