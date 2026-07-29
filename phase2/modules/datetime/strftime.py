from datetime import datetime

dates = [
    datetime(1995, 6, 15),
    datetime(1990, 12, 25),
    datetime(1988, 3, 8),
    datetime(2000, 9, 21),
]

formats = ["%Y-%m-%d", "%B %d, %Y", "%d/%m/%Y", "%A, %B %d, %Y"]

for date in dates:
    print(f"\n--- {date} ---")
    for fmt in formats:
        print(f"{date.strftime(fmt)}")
