expenses = []

menus = [
    "Add expense",
    "View all expenses",
    "View expenses by category",
    "View summary",
    "Exit",
]


def print_expense(expense):
    print(
        f"{expense["Description"]} - ${expense["Amount"]:.2f} ({expense["Category"]})"
    )


def get_unique_category():
    unique_category = set()

    for expense in expenses:
        unique_category.add(expense.get("Category"))

    return unique_category


def amounts_list():
    amount = []

    for expense in expenses:
        amount.append(expense["Amount"])

    return amount


def print_choices():
    print("\n----- Expense Tracker -----")
    for index, menu in enumerate(menus, start=1):
        print(f"{index}. {menu}")


def add_expense():
    description = input("\nEnter description of expense: ")
    amount = float(input("Enter amount of the expense: "))
    category = input("Enter category for the expense: ")

    expenses.append(
        {"Description": description, "Amount": amount, "Category": category}
    )


def view_expenses():
    if len(expenses) == 0:
        print("No transactions made!")
    else:
        print("\n----- Expenses -----")
        for expense in expenses:
            print_expense(expense)


def expenses_by_category():
    if len(expenses) == 0:
        print("No transactions made yet!")
    else:
        category = list(get_unique_category())

        print("\n----- Choose Category -----")

        for index, item in enumerate(category, start=1):
            print(f"{index}. {item}")

        while True:
            try:
                choice = int(input("\nWhat category do you wish to see (0 to exit): "))
            except ValueError:
                print("Please enter the number next to the category!")
            else:
                if choice == 0:
                    break
                elif not 1 <= choice <= len(category):
                    print("Unavailable")
                else:
                    print(f"\n----- Showing expenses for {category[choice - 1]} -----")
                    for expense in expenses:
                        if expense["Category"] == category[choice - 1]:
                            print_expense(expense)


def summary():
    if not expenses:
        print("No transactions made yet!")
    else:
        amounts = amounts_list()
        categories = list(get_unique_category())

        print("\n----- Summary -----")
        # total number of expenses
        print(f"Number of expenses: {len(expenses)}")

        # total amount spent
        print(f"Total amount spent: ${sum(amounts):.2f}")

        # most expensive single expense
        most_expensive = expenses[amounts.index(max(amounts))]
        print(
            f"Most expensive: {most_expensive['Description']} - ${most_expensive['Amount']:.2f} ({most_expensive['Category']})"
        )

        # category breakdown (total spent per category)
        total = 0

        for category in categories:
            print(f"\n--- Total for {category} ---")
            for expense in expenses:
                if category == expense["Category"]:
                    print(
                        f"{expense["Description"]} - ${expense["Amount"]:.2f} ({expense["Category"]})"
                    )
                    total += expense["Amount"]
            print("----------------------------")
            print(f"Total for {category}: ${total:.2f}")

            total = 0


while True:
    print_choices()
    try:
        choice = int(input("\nEnter a task you want to perform: "))
    except ValueError:
        print("Please enter the number next to the task!")
    else:
        if choice == 5:
            break
        elif not 1 <= choice <= len(menus):
            print("Menu unavailable!")
        elif choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            expenses_by_category()
        elif choice == 4:
            summary()
