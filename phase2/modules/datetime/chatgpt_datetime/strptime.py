from datetime import datetime

# challenge 1
print("\n--- challenge 1 ---")
date1_str = "2026-08-15"
date_object = datetime.strptime(date1_str, "%Y-%m-%d").date()

print(type(date_object))


# challenge 2
print("\n--- challenge 2 ---")
dates = [
    "2026-08-15",
    "15/08/2026",
    "August 15, 2026",
    "Aug 15, 2026",
]
new_dates = [
    datetime.strptime(date, fmt).date()
    for date, fmt in zip(dates, ["%Y-%m-%d", "%d/%m/%Y", "%B %d, %Y", "%b %d, %Y"])
]
for d in new_dates:
    print(d)


# challenge 3
print("\n--- challenge 3 ---")
date3_str = "2026-08-15 14:45:30"
date3_obj = datetime.strptime(date3_str, "%Y-%m-%d %H:%M:%S")

print(f"Date object: {date3_obj}")
print(f"Year: {date3_obj.year}")
print(f"Month: {date3_obj.month}")
print(f"Day: {date3_obj.day}")
print(f"Hour: {date3_obj.hour}")
print(f"Minute: {date3_obj.minute}")
print(f"Second: {date3_obj.second}")


# challenge 4
print("\n--- challenge 4 ---")

raw_dates = [
    ("2026-08-15", "%Y-%m-%d"),
    ("15/08/2026", "%d/%m/%Y"),
    ("August 15, 2026", "%B %d, %Y"),
    ("08-15-2026", "%m-%d-%Y"),
]

for date, fmt in raw_dates:
    print(f"{datetime.strptime(date, fmt).date()}")


# challenge 5
print("\n--- challenge 5 ---")
dates5 = [
    "2026-08-15",
    "15/08/2026",
    "banana",
    "2026/15/08",
    "February 30, 2026",
]
dates5_formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%d/%m", "%B %d, %Y"]
new_dates5_obj = []
for date in dates5:
    for fmt in dates5_formats:
        try:
            new_dates5_obj.append(datetime.strptime(date, fmt).date())
            break
        except ValueError:
            continue
    else:
        print(f"Invalid: {date}")
print(new_dates5_obj)
