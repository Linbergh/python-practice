import csv
import helper

CSV_FILE = "students.csv"


def add_students():
    name = input("\nEnter student name: ")
    grades = helper.get_grade()

    if not grades:
        print("\nNo grades entered, student not added!")
        return

    with open(CSV_FILE, "a", newline="") as student_file:
        fieldnames = ["name", "grade"]
        writer = csv.DictWriter(student_file, fieldnames=fieldnames)
        with_content = student_file.tell()

        if not with_content:
            writer.writeheader()

        grade_str = ",".join(str(grade) for grade in grades)

        writer.writerow({"name": name, "grade": grade_str})

    print("\nSuccessfully added student!")


def view_all_students():
    students = helper.student_table()

    if not students:
        print("\nFile not found!")
        return

    print("\n--- All Students ---")
    for student in students:
        helper.print_student(student)


def search_student():
    students = helper.student_table()

    if not students:
        print("\nFile not found!")
        return

    name = input("\nEnter student to search: ").lower()

    student = [student for student in students if student["name"].lower() == name]

    if not student:
        print("\nStudent not found!")
        return

    helper.print_student(student[0])


def top_students():
    students = helper.student_table()

    if not students:
        print("\nFile not found!")
        return

    sorted_students = sorted(
        students, key=lambda student: student["average"], reverse=True
    )

    top_students = sorted_students[0:3]

    print("\n--- Top Students ---")

    for student in top_students:
        helper.print_student(student)


def failing_students():
    students = helper.student_table()

    if not students:
        print("\nFile not found!")
        return

    failing_students = [student for student in students if student["average"] < 60]

    if not failing_students:
        print("\nNo failing students in this class!")

    for student in failing_students:
        helper.print_student(student)


def summary():
    students = helper.student_table()

    if not students:
        print("\nFile not found!")
        return

    averages = [student["average"] for student in students]
    highest_avg = max(averages)
    lowest_avg = min(averages)

    highest_student = [
        student for student in students if student["average"] == highest_avg
    ]
    lowest_student = [
        student for student in students if student["average"] == lowest_avg
    ]

    print("\n--- Summary ---")
    # Total students
    print(f"\nTotal students: {len(students)}")

    # Class average
    print(f"\nClass average: {sum(averages) / len(averages):.2f}")

    # Highest average
    print(f"\nHighest average: ")
    helper.print_student(highest_student[0])

    # Lowest average
    print(f"\nLowest average: ")
    helper.print_student(lowest_student[0])

    # Grade distribution (how many A's, B's, C's, D's, F's)
    print("\nGrade distribution:")
    grades = [grade["letter_grade"] for grade in students]

    for letter in ["A", "B", "C", "D", "F"]:
        # .count() automatically searches the list and returns the total
        count = grades.count(letter)
        print(f"{letter}: {count}")


def exit_program():
    print("\nGoodbye!")
    return False


options = {
    1: ("Add student", add_students),
    2: ("View all students", view_all_students),
    3: ("Search student", search_student),
    4: ("View top 3 students", top_students),
    5: ("View failing students", failing_students),
    6: ("View summary", summary),
    7: ("Exit", exit_program),
}


while True:
    print("\n----- Student Grade Manager -----")
    for number, (text, _) in options.items():
        print(f"{number}. {text}")

    try:
        option = int(input("\nEnter the number next to the option: "))
    except ValueError:
        print("\nPlease enter the number next to the option!")
        continue

    if not 1 <= option <= len(options):
        print("\nOption unavailable!")
    else:
        _, action = options[option]

        result = action()

        if result is False:
            break
