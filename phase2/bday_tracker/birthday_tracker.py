import datetime

birthdays = [
    {"name": "Alice", "birthday": "1995-06-15"},
    {"name": "Bob", "birthday": "1990-12-25"},
    {"name": "Charlie", "birthday": "1988-03-08"},
    {"name": "Diana", "birthday": "2000-09-21"},
    {"name": "Eve", "birthday": "1995-06-15"},
]


def proper_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d")


def get_age(bday):
    today = datetime.date.today()
    age = today.year - bday.year

    if (today.month, today.year) < (bday.month, bday.year):
        age -= 1

    return age


def count_next_birthday(bday):
    today = datetime.date.today()
    bday_count = today.month - bday.month

    return bday_count


bday = proper_date(birthdays[1]["birthday"])
age = get_age(bday)
next_bday = count_next_birthday(bday)


print(next_bday)
# print(bday)
