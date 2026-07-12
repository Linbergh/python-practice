employees = [
    {"name": "Alice", "department": "Engineering", "salary": 95000, "years": 5},
    {"name": "Elice", "department": "Engineering", "salary": 9000, "years": 5},
    {"name": "Bob", "department": "Marketing", "salary": 62000, "years": 2},
    {"name": "Charlie", "department": "Engineering", "salary": 88000, "years": 8},
    {"name": "Diana", "department": "HR", "salary": 71000, "years": 3},
    {"name": "Eve", "department": "Marketing", "salary": 78000, "years": 6},
    {"name": "Frank", "department": "HR", "salary": 65000, "years": 1},
    {"name": "Grace", "department": "Engineering", "salary": 102000, "years": 10},
    {"name": "Hank", "department": "Marketing", "salary": 59000, "years": 4},
]


# Task 1: Sort employees by salary in descending order.
sort_by_salary = sorted(
    employees, key=lambda employee: employee["salary"], reverse=True
)
# print(sort_by_salary)


# Task 2: Sort employees by years of experience in ascending order, and if two employees have the same years, sort them alphabetically by name.
sort_by_experience = sorted(
    employees, key=lambda employee: (employee["years"], employee["name"])
)
# print(sort_by_experience)


# Task 3: Use filter() to get only Engineering department employees.
engineering_department = list(
    filter(lambda employee: employee["department"] == "Engineering", employees)
)
# print(engineering_department)


# Task 4: Use map() to create a new list of just employee names and their salaries as a tuple:
name_salary = list(
    map(lambda employee: (employee["name"], employee["salary"]), employees)
)
# print(name_salary)


# Task 5: Use filter() to get employees who have been with the company more than 3 years AND earn more than $70,000.
three_years_up = list(
    filter(
        lambda employee: employee["years"] > 3 and employee["salary"] > 70000, employees
    )
)
# print(three_years_up)


# Task 6: Use map() to give every employee a 10% salary raise, returning a new list of dictionaries with the updated salary.
salary_increase = list(
    map(
        lambda employee: {
            "name": employee["name"],
            "department": employee["department"],
            "salary": round(employee["salary"] * 1.10),
            "years": employee["years"],
        },
        employees,
    )
)
# print(salary_increase)


# Task 7: Sort the result of Task 6 by department alphabetically, and within the same department sort by salary descending.
sortby_department_and_salary = sorted(
    salary_increase, key=lambda x: (x["department"], -x["salary"])
)
for item in sortby_department_and_salary:
    print(item)
