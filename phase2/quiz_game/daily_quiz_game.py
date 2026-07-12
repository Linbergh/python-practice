import datetime
import random
import csv

TOTAL_QUESTIONS = 5
CSV_FILE = "quiz_results.csv"

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 12 x 12?", "answer": "144"},
    {"question": "What language is this program written in?", "answer": "Python"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {
        "question": "What is the largest planet in the solar system?",
        "answer": "Jupiter",
    },
    {"question": "How many sides does a hexagon have?", "answer": "6"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
]


def load_score():
    try:
        with open(CSV_FILE, "r") as score_file:
            return list(csv.DictReader(score_file))
    except FileNotFoundError:
        return []


def get_questions(questions, total_questions):
    return random.sample(questions, k=total_questions)


def time_taken(duration):
    total_seconds = int(
        duration.total_seconds()
    )  # converts to total seconds as an integer

    minutes = total_seconds // 60  # how many whole minutes
    seconds = total_seconds % 60  # remaining seconds after removing minutes

    if minutes > 0:
        duration_str = f"{minutes} minute{'s' if minutes != 1 else ''} and {seconds} second{'s' if seconds != 1 else ''}"
    else:
        duration_str = f"{seconds} second{'s' if seconds != 1 else ''}"

    return duration_str


def print_score(score, duration):

    print("\n--- Quiz Complete ---")
    print(f"Score: {score}/{TOTAL_QUESTIONS}")
    print(f"Time taken: {duration}")


def take_quiz(questions_list):
    score = 0
    start = datetime.datetime.now()

    for question in questions_list:
        answer = input(f"\n{question["question"]} ").lower()

        if answer == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"The correct anwer is {question["answer"]}")

    end = datetime.datetime.now()

    duration = end - start
    duration_str = time_taken(duration)
    print_score(score, duration_str)


def check_score():
    scores = load_score()

    if not scores:
        print("\nFile not found!")


questions_list = get_questions(questions, TOTAL_QUESTIONS)
take_quiz(questions_list)
