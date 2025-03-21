import budget_functions as bf  

budget_data = {
    "balance": 500,
    "transactions": [
        {"type": "income", "amount": 1000, "description": "paycheck"},
        {"type": "expense", "amount": 500, "description": "groceries"},
    ]
}


while True:
    print("\nOptions: deposit, expense, balance, history, exit")
    choice = input("Enter your choice: ").strip().lower()

    if choice == "deposit":
        amount = float(input("Enter deposit amount: "))
        description = input("Enter deposit description: ")
        bf.make_deposit(budget_data, amount, description)

    elif choice == "expense":
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        bf.make_expense(budget_data, amount, description)

    elif choice == "balance":
        bf.show_balance(budget_data)

    elif choice == "history":
        bf.show_transaction_history(budget_data)

    elif choice == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid choice, try again.")
