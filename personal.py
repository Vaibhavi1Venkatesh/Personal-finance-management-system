finance = []

def add_entry(entry_type):
    amount = float(input(f"Enter {entry_type} amount: "))
    description = input("Enter description: ")
    finance.append({"type": entry_type, "amount": amount, "description": description})
    print(f"{entry_type} added successfully!")

def view_finances():
    for i, entry in enumerate(finance, 1):
        print(f"{i}. {entry['type']} | ${entry['amount']} | {entry['description']}")

def main():
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Finances\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_entry("Income")
        elif choice == '2':
            add_entry("Expense")
        elif choice == '3':
            view_finances()
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

main()
