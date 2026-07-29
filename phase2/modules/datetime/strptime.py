from datetime import datetime

dates = [
    "1995-06-15",
    "25/12/1990",
    "March 08, 1988",
    "09-21-2000",
]


formats = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%B %d, %Y",
    "%m-%d-%Y",
]


converted_dates = []


for date in dates:
    for fmt in formats:
        try:
            converted_dates.append(datetime.strptime(date, fmt).date())
            break
        except ValueError:
            continue
    else:
        print(f"Could not parse: {date}")


for date in converted_dates:
    print(date)
