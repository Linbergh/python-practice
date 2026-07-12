students = [
    {"name": "Alice", "grades": [92, 88, 95, 79, 84]},
    {"name": "Bob", "grades": [55, 60, 48, 70, 63]},
    {"name": "Charlie", "grades": [78, 82, 74, 88, 91]},
    {"name": "Diana", "grades": [45, 50, 39, 60, 55]},
    {"name": "Eve", "grades": [88, 92, 96, 85, 90]},
    {"name": "Frank", "grades": [61, 58, 72, 65, 70]},
]


def overall_average(students):
    avg_grades = []

    for student in students:
        avg_grade = get_average_grade(student["grades"])
        avg_grades.append(avg_grade)

    return avg_grades


def print_student_data(student, avg, grade):
    print(f"{student} - Average: {avg:.2f} - Grade: {grade}")


def letter_grade(grade):
    if grade > 89:
        return "A"
    elif grade > 79:
        return "B"
    elif grade > 69:
        return "C"
    elif grade > 59:
        return "D"
    else:
        return "F"


def get_average_grade(grade):
    return sum(grade) / len(grade)


def all_student(students):
    print("----- All students -----")
    for student in students:
        avg_grade = get_average_grade(student["grades"])
        grade = letter_grade(avg_grade)

        print_student_data(student["name"], avg_grade, grade)


def top_performing_student(students):
    avg_grades_list = overall_average(students)

    highest = max(avg_grades_list)
    highest_student = students[avg_grades_list.index(highest)]["name"]
    grade = letter_grade(highest)

    print("\n----- Top Performing Student -----")
    print_student_data(highest_student, highest, grade)


def lowest_performing_student(students):
    avg_grades_list = overall_average(students)

    lowest = min(avg_grades_list)
    lowest_student = students[avg_grades_list.index(lowest)]["name"]
    grade = letter_grade(lowest)

    print("\n----- Lowest Performing Student -----")
    print_student_data(lowest_student, lowest, grade)


def passing_students(avg_grades_list):
    for index, average in enumerate(avg_grades_list):
        if average >= 60:
            grade = letter_grade(average)
            student = students[index]["name"]
            print_student_data(student, average, grade)


def failing_students(avg_grades_list):
    for index, average in enumerate(avg_grades_list):
        if average < 60:
            grade = letter_grade(average)
            student = students[index]["name"]
            print_student_data(student, average, grade)


def class_summary(students):
    avg_grades_list = overall_average(students)
    class_average = sum(avg_grades_list) / len(avg_grades_list)

    print("\n----- Summary -----")
    # Number of students
    print(f"Total number of students: {len(students)}")

    # Class average
    print(f"Class average grade: {round(class_average,2)}")

    # passing and failing students (how many and who they are)
    passing_counter = 0
    failing_counter = 0
    for avg in avg_grades_list:
        if avg >= 60:
            passing_counter += 1
        else:
            failing_counter += 1

    print("\n----- Passing Students -----")
    print(f"Number of passing students: {passing_counter}")
    passing_students(avg_grades_list)

    print("\n----- Failing Students -----")
    print(f"Number of failing students: {failing_counter}")
    failing_students(avg_grades_list)


all_student(students)
top_performing_student(students)
lowest_performing_student(students)
class_summary(students)


while True:
    try:
        name = input("\nEnter student name to search (or type exit to exit): ")
    except ValueError:
        print("Please enter a name of the student")
    except Exception as e:
        print(e)
    else:
        if name == "exit":
            break
        else:
            found = False

            for student in students:
                if student["name"] == name:
                    found = True
                    break

            if found:
                avg_grade = get_average_grade(student["grades"])
                grade = letter_grade(avg_grade)
                print_student_data(student["name"], avg_grade, grade)
            else:
                print("Student not found!")
