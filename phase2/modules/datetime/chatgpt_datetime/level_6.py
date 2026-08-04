from datetime import date, datetime

today = date.today()

birthdays = [
    "2008-07-15",
    "1999-02-27",
    "2010-12-01",
    "1985-06-10",
    "2025-12-25",
]


def print_header(number):
    print(f"\n--- challenge {number} ---")


def enriched_birthdays(birthdays):
    enriched = []
    for birthday in birthdays:
        enriched.append(datetime.strptime(birthday, "%Y-%m-%d"))

    return enriched


def is_adult(birthday, today):
    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age = (today.year - 1) - birthday.year

    return age, "Minor" if age < 18 else "Adult"


def days_until_birthday(birthday, today):
    birthday = date(today.year, birthday.month, birthday.day)

    until_bday = birthday - today

    if (today.month, today.day) > (birthday.month, birthday.day):
        until_bday = date(today.year + 1, birthday.month, birthday.day) - today

    return until_bday.days


def subscription_status(subscription, today):
    subscription = datetime.strptime(subscription, "%Y-%m-%d").date()

    if subscription > today:
        return "Active"
    elif subscription == today:
        return "Expires today"
    else:
        return "Expired"


def get_years_of_service(employment_date, today):
    employment_date = datetime.strptime(employment_date, "%Y-%m-%d").date()
    service = today.year - employment_date.year

    if (today.month, today.day) < (employment_date.month, employment_date.day):
        service = (today.year - 1) - employment_date.year

    return service


enriched_bdays = enriched_birthdays(birthdays)

# challenge 1
print_header(1)

for birthday in enriched_bdays:
    age, category = is_adult(birthday, today)
    print(f"{birthday.date()} -> {age} -> {category}")


# challenge 2
print_header(2)

for birthday in enriched_bdays:
    print(birthday.date())
    print(f"Days until next birthday: {days_until_birthday(birthday, today)} days\n")


# challenge 3
print_header(3)

subscriptions = [
    ("Alice", "2026-08-20"),
    ("Bob", "2026-07-15"),
    ("Charlie", "2026-12-01"),
    ("Diana", "2026-08-04"),
]

for name, subscription in subscriptions:
    print(f"{name} - {subscription_status(subscription, today)}")


# challenge 4
print_header(4)

events = [
    ("Conference", "2026-11-15"),
    ("Meeting", "2026-08-10"),
    ("Workshop", "2026-09-01"),
    ("Hackathon", "2026-08-05"),
]

chronological_order = sorted(
    events, key=lambda event: datetime.strptime(event[1], "%Y-%m-%d")
)

for event, day in chronological_order:
    print(f"{event}: {day}")


# challenge 5
print_header(5)

next_event = min(chronological_order, key=lambda event: event[1])
event, day = next_event
day_gap = (datetime.strptime(day, "%Y-%m-%d").date() - today).days

print("Next Event:")
print(event)
print(day)
print(f"{day_gap} {'days' if day_gap > 1 else 'day'} away")


# challenge 6
print_header(6)

employees = [
    ("Alice", "2018-06-10"),
    ("Bob", "2021-09-01"),
    ("Charlie", "2015-01-20"),
    ("Diana", "2024-03-15"),
    ("Bins", "2024-08-26"),
]

for employee, employment_date in employees:
    print(f"{employee} - {get_years_of_service(employment_date, today)} year/s")
