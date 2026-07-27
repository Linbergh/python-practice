employees = [
    {"name": "Alice", "department": "Engineering", "salary": 95000, "years": 5},
    {"name": "Bob", "department": "Marketing", "salary": 62000, "years": 2},
    {"name": "Charlie", "department": "Engineering", "salary": 88000, "years": 8},
    {"name": "Diana", "department": "HR", "salary": 71000, "years": 3},
    {"name": "Eve", "department": "Marketing", "salary": 78000, "years": 6},
    {"name": "Frank", "department": "HR", "salary": 65000, "years": 1},
    {"name": "Grace", "department": "Engineering", "salary": 102000, "years": 10},
    {"name": "Hank", "department": "Marketing", "salary": 59000, "years": 4},
]
departments = {department["department"].lower() for department in employees}


def print_section(header, employees):
    print(f"\n--- {header} ---")
    for emp in employees:
        print(
            f"Name: {emp['name']} | Department: {emp['department']}  | Salary: {emp['salary']:,.2f}"
        )


def get_average(x):
    return sum(x) / len(x)


def print_employees_sorted_by_salary(employees):
    sorted_by_salary = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
    print_section("All employees", sorted_by_salary)


def print_highest_lowest_paid_employee(employees):
    highest_paid_employee = max(employees, key=lambda emp: emp["salary"])
    lowest_paid_employee = min(employees, key=lambda emp: emp["salary"])

    print_section("Highest paid employee", [highest_paid_employee])
    print_section("Lowest paid employee", [lowest_paid_employee])


def print_average_salary_accross_employees(employees):
    salaries = [salary["salary"] for salary in employees]
    averaga_salary = get_average(salaries)

    print("\n--- Average salary ---")
    print(f"Average salary: {averaga_salary:,.2f}")


def ask_print_department(employees, departments):
    given_department = input("\nEnter department: ").lower()
    filtered_employees_by_department = []

    if given_department not in departments:
        print("Department not found!")
        return

    for emp in employees:
        if given_department == emp["department"].lower():
            filtered_employees_by_department.append(emp)

    print_section(
        f"Employees in the {given_department.capitalize()} department",
        filtered_employees_by_department,
    )


def print_department_summary(employees, departments):
    for department in departments:
        salaries = [salaries["salary"] for salaries in employees]
        average_salary = get_average(salaries)
        print(average_salary)


# print_employees_sorted_by_salary(employees)
# print_highest_lowest_paid_employee(employees)
# print_average_salary_accross_employees(employees)
# ask_print_department(employees, departments)
print_department_summary(employees, departments)
