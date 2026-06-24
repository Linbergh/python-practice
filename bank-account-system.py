def deposit(amount):
    global balance, transaction
    balance += amount

    transaction.append((amount, "deposit"))

    print(f"Deposited ${amount:.2f}")


def withdraw(amount):
    global balance, transaction

    if balance < amount:
        print("Insufficient funds!")
    else:
        balance -= amount

        transaction.append((amount, "withdrawal"))

        print(f"Withdrawn ${amount:.2f}")


def get_balance():
    global balance

    print(f"\nRemaining balance: ${balance:.2f}")


def transaction_history():
    print("\n--- Transaction History ---")
    for amount, type in transaction:
        if type == "deposit":
            print(f"+ ${amount:.2f} ({type})")
        else:
            print(f"- ${amount:.2f} ({type})")
    print("---------------------------")


balance = 0
transaction = []


deposit(50)
deposit(100)
withdraw(30)
withdraw(200)
transaction_history()
get_balance()
