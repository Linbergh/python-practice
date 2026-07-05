import csv

MAX_GRADES = 5
CSV_FILE = "students.csv"


def get_grade():
    grades = []
    counter = 1

    while counter <= MAX_GRADES:
        user_grade = input(f"\nEnter grade {counter} (type 'done' to exit): ")

        if user_grade.lower() == "done":
            break

        try:
            grade = int(user_grade)

            if not 0 <= grade <= 100:
                print("\nInvalid grade. Please enter a grade between 0 and 100.")
                continue

            grades.append(grade)

        except ValueError:
            print("\nPlease type a valid grade!")
            continue

        counter += 1
    return grades


def get_average_grade(grades):
    grades = grades.split(",")
    grades_list = [int(grade) for grade in grades]

    return grades_list, sum(grades_list) / len(grades_list)


def get_letter_grade(average):
    if average > 89:
        return "A"
    elif average > 79:
        return "B"
    elif average > 69:
        return "C"
    elif average > 59:
        return "D"
    else:
        return "F"


def load_students():
    try:
        with open(CSV_FILE, "r") as student_file:
            return list(csv.DictReader(student_file))
    except FileNotFoundError:
        return []


def print_student(student):
    print(
        f"{student['name']} - Grades: {student['grade']} - Average: {student['average']:.2f} - Grade: {student['letter_grade']}",
    )


def student_table():
    rows = load_students()

    if not rows:
        return []

    student_table = []

    for row in rows:
        grades_list, average = get_average_grade(row["grade"])
        letter_grade = get_letter_grade(average)

        student_table.append(
            {
                "name": row["name"],
                "grade": grades_list,
                "average": average,
                "letter_grade": letter_grade,
            }
        )

    return student_table
