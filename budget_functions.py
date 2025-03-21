def make_deposit(budget_data, amount, description):
    budget_data["balance"] += amount
    budget_data["transactions"].append({"type": "income", "amount": amount, "description": description})

#adds a functions to make a deposit

def make_expense(budget_data, amount, description):
    if budget_data["balance"] >= amount:
        budget_data["balance"] -= amount
        budget_data["transactions"].append({"type": "expense", "amount": amount, "description": description})
    else:
        print("Insufficient funds!")


def show_balance(budget_data):
    print(f"Current Balance: ${budget_data['balance']}")

#adds a function to show the balance 

def show_transaction_history(budget_data):
    for transaction in budget_data["transactions"]:
        print(f"{transaction['type'].capitalize()}: ${transaction['amount']} - {transaction['description']}")

#adds a function to show the transaction history 

