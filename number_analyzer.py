numbers = [15, 42, 7, 93, 28, 61, 4, 77, 36, 55]

even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]


# All even numbers
print(f"Even numbers: {even_nums}")

# All odd numbers
print(f"Odd numbers: {odd_nums}")


# The highest number
print(f"Highest number: {max(numbers)}")


# The lowest number
print(f"Lowest number: {min(numbers)}")

# The average
print(f"Average: {sum(numbers) / len(numbers)}")
