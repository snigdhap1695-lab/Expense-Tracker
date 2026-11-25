expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append((item, amount))

    elif choice == "2":
        total = 0

        for item, amount in expenses:
            print(f"{item}: ${amount}")
            total += amount

        print(f"Total: ${total}")

    elif choice == "3":
        break