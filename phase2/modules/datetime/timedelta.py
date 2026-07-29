import datetime

start_date = datetime.datetime(2024, 1, 1)
today = datetime.datetime.today()

fmt = "%B %d, %Y"
day_fmt = "%A"

# What date is 30 days after start_date?
print(
    f"30 days after start: {(start_date + datetime.timedelta(days=30)).strftime(fmt)}"
)

# What date is 90 days before start_date?
print(
    f"90 days before start: {(start_date - datetime.timedelta(days=90)).strftime(fmt)}"
)

# What date is 1 year after start_date? (use 365 days)
print(
    f"1 year after start: {(start_date + datetime.timedelta(days=365)).strftime(fmt)}"
)

# How many days are between start_date and today?
print(f"Difference between start and today: {(today - start_date).days} days")

# What day of the week will it be 100 days from today?
print(
    f"The day 100 days from now: {(today + datetime.timedelta(days=100)).strftime(day_fmt)}"
)
