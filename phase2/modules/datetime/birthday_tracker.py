from datetime import date, datetime

birthdays = [
    {"name": "Alice", "birthday": "1995-06-15"},
    {"name": "Bob", "birthday": "1990-12-25"},
    {"name": "Charlie", "birthday": "1988-03-08"},
    {"name": "Diana", "birthday": "2000-09-21"},
    {"name": "Eve", "birthday": "1995-06-15"},
    {"name": "Bins", "birthday": "1999-02-27"},
]
today = date.today()


def parse_birthday(birthday):
    return datetime.strptime(birthday, "%Y-%m-%d").date()


def header(text):
    print(f"\n--- {text} ---")


def get_age(birthday, today):
    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age


def get_days_until_birthday(birthday, today):
    birthday = date(today.year, birthday.month, birthday.day)

    if (today.month, today.day) > (birthday.month, birthday.day):
        birthday = date(today.year + 1, birthday.month, birthday.day)

    return (birthday - today).days


def get_weekday(birthday, today):
    birthday = date(today.year, birthday.month, birthday.day)

    if today > birthday:
        birthday = date(today.year + 1, birthday.month, birthday.day)
        return date.strftime(birthday, "%A")

    return date.strftime(birthday, "%A")


enriched_birthdays = []

for person in birthdays:
    name = person["name"]
    birthday = parse_birthday(person["birthday"])

    enriched_birthdays.append({"name": name, "birthday": birthday})


# print each person
header("Person details")

for person in enriched_birthdays:
    age = get_age(person["birthday"], today)
    days_until_bday = get_days_until_birthday(person["birthday"], today)
    day_next_bday = get_weekday(person["birthday"], today)

    print(f"Name: {person['name']}")
    print(f"Birthday: {date.strftime(person['birthday'], '%B %d, %Y')}")
    print(f"Age: {age} {'years' if age > 1 else 'year'} old")
    print(
        f"Days until next birthday: {days_until_bday} {'days' if days_until_bday > 1 else 'day'}"
    )
    print(f"Next birthday falls on a: {day_next_bday}\n")


# nearest upcoming birthday
header("Nearest upcoming birthday")
