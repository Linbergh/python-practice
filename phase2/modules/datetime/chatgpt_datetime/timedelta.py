from datetime import date, timedelta

today = date.today()

# challenge 1
print("\n--- challenge 1 ---")
print(f"Today: {today}")
print(f"Tomorrow: {today + timedelta(days=1)}")
print(f"Yesterday: {today - timedelta(days=1)}")


# challenge 2
print("\n--- challenge 2 ---")
start = date(2026, 8, 15)
for days in [7, 30, 90, 365]:
    print(f"{days} days later: {start + timedelta(days=days)}")


# challenge 3
print("\n--- challenge 3 ---")
for days in [7, 30, 90, 365]:
    print(f"{days} days earlier: {start - timedelta(days=days)}")


# challenge 4
print("\n--- challenge 4 ---")
christmas = date(today.year, 12, 25)

if today > christmas:
    christmas = date(today.year + 1, 12, 25)

days_left = (christmas - today).days
print(f"Days until Christmas: {days_left} days")


# challenge 5
print("\n--- challenge 5 ---")
project_start = date(2026, 1, 10)
project_end = date(2026, 4, 25)

print(f"Project started: {project_start}")
print(f"Project ended: {project_end}")
print(f"Project duration: {(project_end - project_start).days} days")


# challenge 6
print("\n--- challenge 6 ---")
loan_date = date(2026, 8, 3)

for due in [30, 60, 90, 180]:
    print(f"{due}-day loan: {loan_date + timedelta(days=due)}")
