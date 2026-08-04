from datetime import date, datetime

today = date.today()

employees = [
    {
        "name": "Alice",
        "birthday": "1998-06-10",
        "hire_date": "2018-06-10",
    },
    {
        "name": "Bob",
        "birthday": "2002-11-15",
        "hire_date": "2021-09-01",
    },
    {
        "name": "Charlie",
        "birthday": "1987-01-20",
        "hire_date": "2015-01-20",
    },
]


def print_employee(name, age, years_of_service, next_bday):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Years of Service: {years_of_service}")
    print(f"Next Birthday: {next_bday} days\n")


def completed_years(start_date, today):
    years = today.year - start_date.year

    if (today.month, today.day) < (start_date.month, start_date.day):
        years -= 1

    return years


def next_birthday(birthday, today):
    birthday = date(today.year, birthday.month, birthday.day)

    until_bday = birthday - today

    if birthday < today:
        until_bday = date(today.year + 1, birthday.month, birthday.day) - today

    return until_bday.days


def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()


for employee in employees:
    birthday = parse_date(employee["birthday"])
    hire_date = parse_date(employee["hire_date"])

    age = completed_years(birthday, today)
    years_in_service = completed_years(hire_date, today)
    next_bday = next_birthday(birthday, today)

    print_employee(employee["name"], age, years_in_service, next_bday)
