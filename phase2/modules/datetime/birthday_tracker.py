from datetime import date, datetime

today = date.today()
birthdays = [
    {"name": "Alice", "birthday": "1995-06-15"},
    {"name": "Bob", "birthday": "1990-12-25"},
    {"name": "Charlie", "birthday": "1988-03-08"},
    {"name": "Diana", "birthday": "2000-09-21"},
    {"name": "Eve", "birthday": "1995-06-15"},
    {"name": "Bins", "birthday": "1999-02-27"},
]


def parse_birthday(birthday):
    return datetime.strptime(birthday, "%Y-%m-%d").date()


def header(text):
    print(f"--- {text} ---")


def print_person_details(person):
    print(f"Name: {person['name']}")
    print(f"Birthday: {date.strftime(person['birthday'], '%B %d, %Y')}")
    print(f"Age: {person['age']} {'years' if person['age'] > 1 else 'year'} old")
    print(
        f"Days until next birthday: {person['days_until_bday']} {'days' if person['days_until_bday'] > 1 else 'day'}"
    )
    print(f"Next birthday falls on a: {person['day_next_bday']}\n")


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
    birthday = parse_birthday(person["birthday"])

    age = get_age(birthday, today)
    days_until_bday = get_days_until_birthday(birthday, today)
    day_next_bday = get_weekday(birthday, today)

    enriched_birthdays.append(
        {
            "name": person["name"],
            "birthday": birthday,
            "age": age,
            "days_until_bday": days_until_bday,
            "day_next_bday": day_next_bday,
        }
    )


# print each person
header("Person details")

for person in enriched_birthdays:
    print_person_details(person)

# nearest upcoming birthday
header("Nearest upcoming birthday")

nearest_bday = min(enriched_birthdays, key=lambda person: person["days_until_bday"])

print_person_details(nearest_bday)


# oldest and youngest
header("oldest person")
oldest = max(enriched_birthdays, key=lambda person: person["age"])
print_person_details(oldest)


header("youngest person")
youngest = min(enriched_birthdays, key=lambda person: person["age"])
print_person_details(youngest)


# shares the same birthday
grouped = {}

for person in enriched_birthdays:
    key = person["birthday"]

    if key not in grouped:
        grouped[key] = [person["name"]]
    else:
        grouped[key].append(person["name"])

header("Shared Birthdays")
for birthday, names in grouped.items():
    if len(names) > 1:
        print(f"{date.strftime(birthday, '%B %d, %Y')}: {', '.join(names)}")
