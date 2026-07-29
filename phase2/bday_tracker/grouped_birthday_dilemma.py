grouped_birthdays = {
    "1995-06-15": ["Alice", "Eve"],
    "1990-12-25": ["Bob"],
    "1988-03-08": ["Charlie"],
    "2000-09-21": ["Diana"],
}


def shared_birthdays(birthdays):

    with_shared_birthday = [
        birthday for birthday in birthdays.items() if len(birthday[1]) > 1
    ]

    for shared in with_shared_birthday:
        for names in shared[1]:
            print(f"Birthday: {shared[0]} - Names: {names}")


shared_birthdays(grouped_birthdays)
