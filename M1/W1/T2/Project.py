bal = 50000
pin = "arya7"

while True:
    print("\nATM Menu")
    print("1. Cash Withdrawal")
    print("2. Balance Enquiry")
    print("3. Change PIN")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        if amount <= bal:
            bal -= amount
            print("Processing done")
            print(f"Remaining balance: {bal}")
        else:
            print("Insufficient balance")

    elif choice == 2:
        print(f"Available balance: {bal}")

    elif choice == 3:
        pin_check = input("Enter old pin: ")
        if pin_check == pin:
            new_pin = input("Enter new pin: ")
            pin = new_pin
            print("PIN changed")
        else:
            print("Invalid PIN")

    elif choice == 4:
        print("Exiting menu...")
        break

    else:
        print("Invalid choice")