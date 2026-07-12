from helper import letter_grade

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

scores = {"Alice": 92, "Bob": 55, "Charlie": 78, "Diana": 45, "Eve": 88}

products = [
    {"name": "Apple", "price": 1.20},
    {"name": "Bread", "price": 2.50},
    {"name": "Milk", "price": 1.80},
    {"name": "Eggs", "price": 3.00},
    {"name": "Butter", "price": 4.50},
]


# Task 1: From students, create a dictionary where each student's name is the key and the length of their name is the value:
name_length = {student: len(student) for student in students}
print(name_length)

# Task 2: From scores, create a new dictionary containing only students who are passing (60 and above).
passing_students = {student: score for student, score in scores.items() if score >= 60}
print(passing_students)

# Task 3: From scores, create a new dictionary where every score is converted to a letter grade (reuse your letter_grade() function from before).
converted_grade = {key: letter_grade(value) for key, value in scores.items()}
print(converted_grade)

# Task 4: From products, create a dictionary where the product name is the key and the price is the value:
new_products = {product["name"]: product["price"] for product in products}
print(new_products)

# Task 5: From products, create a dictionary where the product name is the key and the price is the value,
# but only for products that cost more than $2.00, and increase their price by 10%.
two_dollars_up = {
    product["name"]: round(product["price"] * 1.1, 2)
    for product in products
    if product["price"] > 2
}
print(two_dollars_up)
