import csv

EXPENSES_FILE = "expenses.csv"


def display_expenses(options):
    print("\n----- Expense Tracker -----")

    for number, (text, _) in options.items():
        print(f"{number}. {text}")


def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as csv_file:
            return list(csv.DictReader(csv_file))
    except FileNotFoundError:
        return []


def add_expense():
    description = input("\nEnter description of expense: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    with open(EXPENSES_FILE, "a", newline="") as csv_file:
        fieldnames = ["description", "amount", "category"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        with_content = csv_file.tell()

        if not with_content:
            writer.writeheader()

        writer.writerow(
            {"description": description, "amount": amount, "category": category}
        )

    print("\nSuccessfully added expense!")


def view_all_expenses():
    rows = load_expenses()

    if not rows:
        print("\nNo expenses yet!")
        return

    print("\n--- All Expenses ---")
    for index, row in enumerate(rows, start=1):
        print(
            f"{index}. {row['description']} - ${float(row['amount']):.2f} ({row['category']})"
        )


def view_by_category():
    rows = load_expenses()

    if not rows:
        print("\nNo expenses yet!")
        return

    categories = list(sorted(set(row["category"] for row in rows)))

    while True:
        print("\n----- Categories -----")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        try:
            category = int(input("\nEnter category(0 to exit): "))

            if category == 0:
                break

            if not 1 <= category <= len(categories):
                print(f"\nPlease select the number next to the category!")
                continue
            else:
                total = 0

                selected_category = categories[category - 1]

                print(f"\nShowing expenses by: {selected_category}\n")

                expenses_by_category = [
                    row for row in rows if row["category"] == selected_category
                ]

                for item in expenses_by_category:
                    print(
                        f"{item['description']} - ${float(item['amount']):.2f} ({item['category']})"
                    )
                    total += float(item["amount"])

                print("-------------------------")
                print(f"Total: ${total:.2f}")
        except ValueError:
            print("\nPlease enter the number next to the category.")


def view_summary():
    rows = load_expenses()

    if not rows:
        print("\nNo expenses yet!")
        return

    amount_expenses = [float(row["amount"]) for row in rows]

    max_expensive = max(amount_expenses)
    most_expensive = [row for row in rows if float(row["amount"]) == max_expensive]

    # Total number of expenses
    print(f"\nTotal number of expenses: {len(rows)}")

    # Total amount spent
    print(f"\nTotal amount spent: ${sum(amount_expenses):.2f}")

    # Most expensive single expense
    print("\nMost expensive single expense:")
    for item in most_expensive:
        print(f"{item['description']} - ${item['amount']} ({item['category']})")

    # Category breakdown
    total = 0
    print("\nExpenses by category")
    categories = list(sorted(set(row["category"] for row in rows)))

    for category in categories:
        print(f"\n--- {category} ---")
        for row in rows:
            if row["category"] == category:
                print(
                    f"{row['description']} - ${float(row['amount']):.2f} ({row['category']})"
                )

                total += float(row["amount"])

        print(f"Total: ${total:.2f}")
        total = 0


def clear_expenses():
    rows = load_expenses()

    if not rows:
        print("\nNo expenses to clear!")
        return

    answer = input("\nAre you sure? (yes/no): ").lower().strip()

    if answer == "yes":
        with open(EXPENSES_FILE, "w", newline="") as csv_file:
            pass

        print("\nCleared expenses successfully!")


def exit_program():
    print("\nGoodbye!")
    return False


options = {
    1: ("Add expense", add_expense),
    2: ("View all expenses", view_all_expenses),
    3: ("View expenses by category", view_by_category),
    4: ("View summary", view_summary),
    5: ("Clear all expenses", clear_expenses),
    6: ("Exit", exit_program),
}


while True:
    display_expenses(options)

    try:
        option = int(input("\nEnter the number next to the option: "))
    except ValueError:
        print("\nPlease enter the number next to the option!")
        continue

    if not 1 <= option <= len(options):
        print("\nOption unavailable!")
    else:
        _, action = options[option]

        result = action()

        if result is False:
            break
