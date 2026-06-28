numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

words = ["hello", "world", "python", "is", "fun", "list", "comprehension", "rocks"]

students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 55},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 45},
    {"name": "Eve", "grade": 88},
]

# Task 1: From numbers, create a new list containing only the even numbers.
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Task 2: From numbers, create a new list where every number is squared.
squared = [num * num for num in numbers]  # num ** 2 can replace num * num
print(squared)

# Task 3: From words, create a new list containing only words longer than 4 characters.
four_letter_word = [word for word in words if len(word) > 4]
print(four_letter_word)

# Task 4: From words, create a new list where every word is uppercased.
all_caps = [word.upper() for word in words]
print(all_caps)

# Task 5: From students, create a new list containing only the names of students who are passing (grade 60 and above).
passing_students = [student["name"] for student in students if student["grade"] >= 60]
print(passing_students)
