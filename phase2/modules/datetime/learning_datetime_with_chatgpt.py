import datetime

today = datetime.datetime.now(datetime.UTC)

# today's date
print(f"\nToday's date: {today.date()}")

# current time
print(f"\nCurrent time: {today.strftime('%I:%M:%S')}")

# Birthday
my_birthday = datetime.date(1999, 2, 27)
print(f"\nBirthday: {my_birthday}")
print(f"Year: {my_birthday.year}")
print(f"Month: {my_birthday.month}")
print(f"Day: {my_birthday.day}")

# appointment
appointment = datetime.datetime(2026, 12, 25, 20, 30, tzinfo=datetime.timezone.utc)
print(f"\nAppointment date: {appointment.strftime('%B %d, %Y')}")
print(f"Appointment time: {appointment.strftime('%I:%M %p')}")


meeting = datetime.datetime(2026, 8, 15, 14, 45, 30, tzinfo=datetime.timezone.utc)
print("\n--- meeting details ---")
print(f"year: {meeting.year}")
print(f"month: {meeting.month}")
print(f"day: {meeting.day}")
print(f"hour: {meeting.hour}")
print(f"minute: {meeting.minute}")
print(f"second: {meeting.second}")
print(f"weekday: {meeting.weekday()}")
print(f"iso weekday: {meeting.isoweekday()}")


dates = [
    datetime.date(2026, 1, 1),
    datetime.date(2026, 4, 15),
    datetime.date(2026, 12, 27),
]


def is_iso_weekend(day):
    return day in (6, 7)


def get_quarter(month):
    quarter = [
        {"quarter": 1, "month_number": [1, 2, 3]},
        {"quarter": 2, "month_number": [4, 5, 6]},
        {"quarter": 3, "month_number": [7, 8, 9]},
        {"quarter": 4, "month_number": [10, 11, 12]},
    ]

    for qrtr in quarter:
        if month in qrtr["month_number"]:
            return qrtr["quarter"]

    # arithmetic way
    # return (month - 1) // 3 + 1


print("\n--- dates ---")
for date in dates:
    print(f"\nDate: {date}")
    print(f"Day number: {date.day}")
    print(f"Month number: {date.month}")
    print(f"Quarter: {get_quarter(date.month)}")
    print(f"Weekend?: {'Yes' if is_iso_weekend(date.isoweekday()) else 'No'}")
