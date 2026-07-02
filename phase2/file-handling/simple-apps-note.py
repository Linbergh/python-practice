def print_options(actions):
    print("\n----- Notes App -----")

    for number, (text, _) in actions.items():
        print(f"{number}. {text}")


def add_note():
    note = input("\nEnter note: ")

    with open("notes.txt", "a") as notes_file:
        notes_file.write(f"{note}\n")


def view_notes():
    try:
        print("\n----- Your Notes -----")

        with open("notes.txt", "r") as notes_file:
            reader = notes_file.readlines()

            if len(reader) <= 0:
                print("\nNo notes yet!")
            else:
                for number, line in enumerate(reader, start=1):
                    print(f"{number}. {line}", end="")

    except FileNotFoundError:
        print("\nFile not found!")


def clear_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()

            if not content:
                print("\nNo notes to clear!")
                return

        answer = input("\nAre you sure? (yes/no): ").strip()

        if answer.lower() == "yes":
            with open("notes.txt", "w") as notes_file:
                notes_file.write("")
            print("\nNotes cleared!")
        else:
            print("\nCancelled!")

    except FileNotFoundError:
        print("\nNo notes to clear!")


def exit_program():
    print("Goodbye!")
    return False


actions = {
    1: ("Add note", add_note),
    2: ("View all notes", view_notes),
    3: ("Clear all notes", clear_notes),
    4: ("Exit", exit_program),
}

while True:
    print_options(actions)

    try:
        option = int(input("\nEnter the number next to the option: "))
    except ValueError:
        print("\nPlease enter the number next to the option!")
        continue

    if not 1 <= option <= len(actions):
        print("\nOption unavailable!")
    else:
        _, action = actions[option]

        result = action()

        if result is False:
            break
