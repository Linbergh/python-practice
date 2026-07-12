numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6, 10]

words = ["banana", "apple", "kiwi", "strawberry", "mango", "blueberry"]

students = [
    {"name": "Alice", "grade": 92, "age": 20},
    {"name": "Bob", "grade": 55, "age": 22},
    {"name": "Charlie", "grade": 78, "age": 19},
    {"name": "Diana", "grade": 45, "age": 21},
    {"name": "Eve", "grade": 88, "age": 18},
    {"name": "Adan", "grade": 88, "age": 18},
]

products = [
    {"name": "Apple", "price": 1.20},
    {"name": "Bread", "price": 2.50},
    {"name": "Milk", "price": 1.80},
    {"name": "Eggs", "price": 3.00},
    {"name": "Butter", "price": 4.50},
]

# Task 1: Sort numbers in descending order using sorted() and a lambda.
numbers_desc = sorted(numbers, key=lambda num: num, reverse=True)
print(numbers_desc)

# Task 2: Sort words by word length (shortest to longest) using sorted() and a lambda.
sorted_by_word_length = sorted(words, key=lambda word: len(word))
print(sorted_by_word_length)

# Task 3: Use map() and a lambda to create a new list where every number in numbers is squared.
squared = list(map(lambda num: num**2, numbers))
print(squared)

# Task 4: Use filter() and a lambda to create a new list containing only words longer than 5 characters.
long_word = list(filter(lambda word: len(word) > 5, words))
print(long_word)

# Task 5: Sort students by grade in descending order using a lambda.
students_desc = sorted(students, key=lambda student: student["grade"], reverse=True)
print(students_desc)

# Task 6: Sort products by price in ascending order using a lambda.
products_asc = sorted(products, key=lambda product: product["price"])
print(products_asc)

# Task 7: Sort students by age in ascending order, and if two students have the same age, sort them alphabetically by name. (Hint: your lambda can return a tuple of two values)
students_by_age = sorted(
    students, key=lambda student: (student["age"], student["name"])
)
print(students_by_age)
