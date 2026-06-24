def deposit(amount):
    global balance, transaction
    balance += amount

    transaction.append((amount, "deposit"))


def withdraw(amount):
    global balance, transaction
    balance -= amount

    transaction.append((amount, "withdrawal"))


def get_balance(amount):
    pass


def transcation_history():
    print("--- Transaction History ---")
    for amount, type in transaction:
        if type == "Deposit":
            print(f"+ ${amount:.2f} ({type})")
        else:
            print(f"- ${amount:.2f} ({type})")
    print("---------------------------")


balance = 0
transaction = []


deposit(50)
withdraw(25)
transcation_history()
