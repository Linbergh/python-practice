import datetime

meeting = datetime.datetime(2026, 8, 11, 14, 45, 30, tzinfo=datetime.timezone.utc)

date_formats = ["%m/%d/%Y", "%d/%m/%Y", "%B %d, %Y", "%b %d, %Y"]
time_formats = ["%H:%M", "%H:%M:%S", "%I:%M %p", "%I:%M:%S %p"]
full_date_time_formats = ["%A, %B %d, %Y", "%A, %B %d, %Y at %I:%M %p"]
# own_formats = ["%Y/%B/%d", "%a - %b %d", "%B, %Y", "%dth of %B, %Y"]


def get_suffix(day):
    suffix = {1: "st", 2: "nd", 3: "rd"}

    if 11 <= (day % 100) <= 13:
        return "th"

    return suffix.get(day % 10, "th")


own_formats = [
    "%Y/%B/%d",
    "%a - %b %d",
    "%B, %Y",
    f"%d{get_suffix(meeting.day)} of %B, %Y",
]


#  challenge 1. Basic Formatting
print(meeting.strftime("%Y-%m-%d"))

# challenge 2 Different Date Styles
print("\n--- Different Date Styles ---")
for date_fmt in date_formats:
    print(meeting.strftime(date_fmt))


# challenge 3 Time formats
print("\n--- Time formats ---")
for time_fmt in time_formats:
    print(meeting.strftime(time_fmt))


# Challenge 4 Full date and time
print("\n--- Full date and time ---")
for full_fmt in full_date_time_formats:
    print(meeting.strftime(full_fmt))


# Challenge 5 own format
print("\n--- own format ---")
for own_fmt in own_formats:
    print(meeting.strftime(own_fmt))
