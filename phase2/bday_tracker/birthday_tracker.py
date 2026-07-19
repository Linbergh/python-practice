import datetime

birthdays = [
    {"name": "Alice", "birthday": "1995-06-15"},
    {"name": "Bob", "birthday": "1990-12-25"},
    {"name": "Charlie", "birthday": "1988-03-08"},
    {"name": "Diana", "birthday": "2000-09-21"},
    {"name": "Eve", "birthday": "1995-06-15"},
]


def proper_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()


def get_age(bday):
    today = datetime.date.today()
    age = today.year - bday.year

    if (today.month, today.day) < (bday.month, bday.day):
        age -= 1

    return age


def count_days(bday):
    today = datetime.date.today()
    birthday = proper_date(bday)

    next_birthday = birthday.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    return (next_birthday - today).days


def person_details(birthdays):
    enriched = []

    for birthday in birthdays:
        age = get_age(proper_date(birthday["birthday"]))
        n_days = count_days(birthday["birthday"])
        bday = proper_date(birthday["birthday"])
        enriched.append(
            {
                "name": birthday["name"],
                "birthday": bday,
                "age": age,
                "days_until_bday": n_days,
            }
        )

    return enriched


def print_section(header, birthdays):
    print(f"--- {header} ---")
    for bday in birthdays:
        print(
            f"{bday['name']}\n"
            f" Birthday: {bday['birthday'].strftime('%B %d, %Y')}\n"
            f" Age: {bday['age']} years old\n"
            f" Days until next birthday: {bday['days_until_bday']}\n"
        )


def pritn_person(header, detail):
    print(f"--- {header} ---")
    print(
        f"{detail['name']}\n"
        f" Birthday: {detail['birthday'].strftime('%B %d, %Y')}\n"
        f" Age: {detail['age']} years old\n"
        f" Days until next birthday: {detail['days_until_bday']}\n"
    )


def get_nearest_bday(birthdays):
    return min(birthdays, key=lambda bday: bday["days_until_bday"])


def get_oldest(birthdays):
    return max(birthdays, key=lambda bday: bday["age"])


def get_youngest(birthdays):
    return min(birthdays, key=lambda bday: bday["age"])


def group_birthdays(birthdays):
    pass


enriched_birthdays = person_details(birthdays)


# print_section("Personal Details", enriched_birthdays)
# pritn_person("Nearest upcoming birthday", get_nearest_bday(enriched_birthdays))
# pritn_person("Oldest", get_oldest(enriched_birthdays))
# pritn_person("Youngest", get_youngest(enriched_birthdays))
group_birthdays(enriched_birthdays)
