options = ["Write a new entry", "View all entries", "Exit"]


def print_options():
    print("\n----- Diary -----")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


def write_entry():
    entry = input("\nEnter entry: ")

    with open("diary.txt", "a") as diary:
        diary.write(f"{entry}\n")


def view_entires():
    try:
        with open("diary.txt", "r") as diary:
            diary = diary.readlines()

            print("\n--- Your Diary Entries ---")

            for index, line in enumerate(diary, start=1):
                print(f"{index}. {line}", end="")
    except FileNotFoundError:
        print("\nNo entries yet!")


while True:
    print_options()
    try:
        option = int(input("\nWhat option do you choose: "))

    except ValueError:
        print("select the number next to the item")
    else:
        if option == 3:
            break

        if not 1 <= option <= len(options):
            print("please select the number next to the option")
        elif option == 1:
            write_entry()
        else:
            view_entires()
