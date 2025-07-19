
transactions = []

def add_income():
    amount = float(input("Enter income amount: "))
    transactions.append({"type": "income", "amount": amount})
    print("Income added!\n")

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    transactions.append({"type": "expense", "amount": amount, "category": category})
    print("Expense added!\n")

def view_summary():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = [t for t in transactions if t["type"] == "expense"]
    total_expense = sum(t["amount"] for t in expenses)
    
    print(f"\nIncome: ₹{income}")
    print("Expenses:")
    for t in expenses:
        print(f"  - {t['category']}: ₹{t['amount']}")
    print(f"Balance: ₹{income - total_expense}\n")

def main():
    while True:
        print("----- Budget Tracker -----")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
