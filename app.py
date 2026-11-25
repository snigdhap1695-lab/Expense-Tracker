import json
import os

FILE_NAME = "expenses.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
else:
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

        expenses.append({
            "item": item,
            "amount": amount
        })

        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

    elif choice == "2":
        total = 0

        for expense in expenses:
            print(f"{expense['item']}: ${expense['amount']}")
            total += expense["amount"]

        print(f"Total: ${total}")

    elif choice == "3":
        break