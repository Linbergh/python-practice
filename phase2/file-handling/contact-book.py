import csv

options = ["Add contact", "View all contacts", "Search contact by name", "Exit"]


def print_options():
    print("\n----- Contact Book -----")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")

    with open("contacts.csv", "a+", newline="") as contacts_file:
        fieldnames = ["name", "phone number", "email"]
        writer = csv.DictWriter(contacts_file, fieldnames=fieldnames, delimiter=",")

        if contacts_file.tell() == 0:
            writer.writeheader()

        writer.writerow({"name": name, "phone number": phone_number, "email": email})

    print("\nSuccessfully added new contact!")


def view_contact():
    try:
        with open("contacts.csv", "r") as contacts_file:
            reader = csv.DictReader(contacts_file)

            print("\n--- All Contacts ---")

            for index, row in enumerate(reader, start=1):
                print(
                    f"{index}. {row['name']} - {row['phone number']} - {row['email']}"
                )

    except FileNotFoundError:
        print("\nNo contacts to show!")
    except KeyError as k_error:
        print(f"error on {k_error}")


def search_contact():
    try:
        name = input("\nEnter name to search: ")

        with open("contacts.csv", "r") as contacts_file:
            reader = csv.DictReader(contacts_file)

            matched = [
                (index, contact)
                for (index, contact) in enumerate(reader, start=1)
                if contact["name"] == name
            ]

            if matched:
                for index, contact in matched:
                    print(
                        f"\n{index}. {contact['name']} - {contact['phone number']} - {contact['email']}"
                    )
            else:
                print("\nContact not found!")
    except FileNotFoundError:
        print("\nNo contacts to show!")


while True:
    print_options()
    try:
        option = int(input("\nWhat option do you choose: "))

    except ValueError:
        print("select the number next to the item")
    else:
        if option == 4:
            break

        if not 1 <= option <= len(options):
            print("\nplease select the number next to the option")
        elif option == 1:
            add_contact()
        elif option == 2:
            view_contact()
        elif option == 3:
            search_contact()
