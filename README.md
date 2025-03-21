# menu
i choose the first option "budget data"

```python 
budget_data = {
    "balance": 500,
    "transactions": [
        {"type": "income", "amount": 1000, "description": "paycheck"},
        {"type": "expense", "amount": 500, "description": "groceries"},
    ]
}

```
i basically did an input command on visual studio for instance 
```python
def add_income(budget_data, amount, description):
def add_expense(budget_data, amount, description):
def show_balance(budget_data):
def show_transaction_history(budget_data):
def exit(budget_data):
"def add_income(budget_data, amount, description):"
we use the add income and the input needs to be budget data - meaning the iteam the amount - for exmaple if its 5 apples so it needs to be mentioned  and the description  - about the item
```
update the data structure based on the received data structure from the function 



```python
def make_deposit(budget_data, amount, description):
    budget_data["balance"] += amount
    budget_data["transactions"].append({"type": "income", "amount": amount, "description": description})
def make_expense(budget_data, amount, description):
    if budget_data["balance"] >= amount:
        budget_data["balance"] -= amount
        budget_data["transactions"].append({"type": "expense", "amount": amount, "description": description})
    else:
        print("Insufficient funds!")

#adds a function to make an expense 

def show_balance(budget_data):
    print(f"Current Balance: ${budget_data['balance']}")

#adds a function to show the balance 

def show_transaction_history(budget_data):
    for transaction in budget_data["transactions"]:
        print(f"{transaction['type'].capitalize()}: ${transaction['amount']} - {transaction['description']}")

#adds a function to show the transaction history 

```

basically an exmaple for the first function it creates a functuion called make depoists and it checks the following parameters budget data, amount and description
afterwords it checks for balance and it add"+=" to the amount for exmaple if the client writes 100 to the existing 500 it adds to the current amount "100" which gets to "600"
then it appends the results 
# in order to make it work one will take each function and reimplament itfor exmaple remake my show_balance into your liking without changing to much of the original function 

# the files i added are already with explantion in the function file and it has a seprate main file with a loop enabled so it ensures the transcation goes clean 
