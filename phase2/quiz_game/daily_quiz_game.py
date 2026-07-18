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


def load_score(csv_file):
    try:
        with open(csv_file, "r") as score_file:
            return list(csv.DictReader(score_file))
    except FileNotFoundError:
        return []


def past_scores():
    scores = load_score(CSV_FILE)

    if not scores:
        print("No previous results.")
    else:
        print("\n--- Past Results ---")
        for index, score in enumerate(scores, start=1):
            date = score["date"]
            result = score["score"]
            total = score["total"]
            duration = score["timetaken"]

            print(f"{index}. Date: {date} | Score: {result}/{total} | Time: {duration}")


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


def get_questions(questions):
    return random.sample(questions, k=TOTAL_QUESTIONS)


def save_score(score, duration, date_taken):

    with open(CSV_FILE, "a", newline="") as score_file:
        fieldnames = ["date", "score", "total", "timetaken"]
        writer = csv.DictWriter(score_file, fieldnames=fieldnames)
        with_content = score_file.tell()

        if not with_content:
            writer.writeheader()

        writer.writerow(
            {
                "date": date_taken,
                "score": score,
                "total": TOTAL_QUESTIONS,
                "timetaken": duration,
            }
        )


def take_quiz(questions_list):
    score = 0
    start = datetime.datetime.now()
    date = datetime.date.today()

    print("\n--- Quiz ---")

    for index, question in enumerate(questions_list, start=1):
        answer = input(f"{index}. {question["question"]} ").lower()

        if answer == question["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"The correct answer is {question["answer"]}\n")

    end = datetime.datetime.now()

    duration = end - start
    duration_str = time_taken(duration)

    print("--- Quiz Complete ---")
    print(f"Score: {score}")
    print(f"Time taken: {duration_str}")
    print(f"Date completed: {date}")

    save_score(score, duration_str, date)


past_scores()
questions_list = get_questions(questions)
take_quiz(questions_list)
