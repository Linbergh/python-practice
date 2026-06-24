balance = 0
transaction = []


def deposit(amount):
    global balance

    if amount <= 0:
        print("Deposit amount must be greater than zero!")
        return

    balance += amount
    transaction.append((amount, "deposit"))
    print(f"Deposited ${amount:.2f} | Balance ${balance:.2f}")


def withdraw(amount):
    global balance

    if amount < 0:
        print("Withdrawal amount must be greater then zero!")
        return
    if amount > balance:
        print("Insufficient funds!")
        return

    balance -= amount
    transaction.append((amount, "withdrawal"))
    print(f"Withdrawn ${amount:.2f} | Balance ${balance:.2f}")


def get_balance():
    print(f"\nCurrent balance: ${balance:.2f}")


def transaction_history():
    if not transaction:
        print("No transactions yet!")
        return

    print("\n--- Transaction History ---")
    for amount, type in transaction:
        symbol = "+" if type == "deposit" else "-"

        print(f"{symbol} ${amount:.2f} ({type})")
    print("---------------------------")


deposit(50)
deposit(100)
withdraw(30)
withdraw(200)
withdraw(-50)
deposit(-20)
transaction_history()
get_balance()
