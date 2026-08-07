from datetime import date, datetime

person = {"name": "Bins", "birthday": "1999-2-27"}
today = date.today()


def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()


def get_age(birthday, today):
    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age


def next_birthday(birthday, today):
    this_year = date(today.year, birthday.month, birthday.day)

    if this_year >= today:
        return this_year

    return date(today.year + 1, birthday.month, birthday.day)


def days_until_next_birthday(birthday, today):
    birthday = date(today.year, birthday.month, birthday.day)

    n_days = birthday - today

    if (today.month, today.day) > (birthday.month, birthday.day):
        n_days = date(today.year + 1, birthday.month, birthday.day) - today

    return n_days.days


def day_of_next_birthday(birthday, today):
    birthday = date(today.year, birthday.month, birthday.day)

    if today > birthday:
        birthday = date(today.year + 1, birthday.month, birthday.day)

    wd = birthday.strftime("%A")

    return wd


birthday = parse_date(person["birthday"])

age = get_age(birthday, today)
next_bday = next_birthday(birthday, today)
days_until_bday = days_until_next_birthday(birthday, today)
wd = day_of_next_birthday(birthday, today)

print(f"Name: {person['name']}")
print(f"Age: {age} years old")
print(f"Next birthday: {next_bday.strftime('%B %d, %Y')}")
print(f"Days until next birthday: {days_until_bday} days")
print(f"Next birthday falls on a: {wd}")
