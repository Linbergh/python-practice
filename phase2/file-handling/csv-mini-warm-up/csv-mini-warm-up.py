import csv

students_list = [("John", 27), ("Maria", 23), ("Doe", 25)]

with open("students.csv", "w", newline="") as students:
    fieldnames = ["name", "age"]

    writer = csv.DictWriter(students, fieldnames=fieldnames, delimiter=",")

    writer.writeheader()

    for name, age in students_list:
        writer.writerow({"name": name, "age": age})


with open("students.csv", "r") as student:
    reader = csv.DictReader(student)

    for row in reader:
        print(row)
