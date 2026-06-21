def get_grade(score):
    if score > 89:
        return "A"
    elif score > 79:
        return "B"
    elif score > 69:
        return "C"
    elif score > 59:
        return "D"
    else:
        return "F"


students = [
    ("Alice", 92),
    ("Bob", 55),
    ("Charlie", 78),
    ("Diana", 45),
    ("Eve", 88),
    ("Frank", 61),
    ("Grace", 39),
    ("Hank", 73),
]

scores = []

for student, score in students:
    grade = get_grade(score)

    print(f"{student} - Score: {score} - Grade: {grade}")

    scores.append(score)

highest = max(scores)
lowest = min(scores)

best_student = students[scores.index(highest)][0]
worst_student = students[scores.index(lowest)][0]

print(f"Highest score: {best_student} with {highest}")
print(f"Lowest score: {worst_student} with {lowest}")
print(f"Average score: {sum(scores) / len(scores):.2f}")
