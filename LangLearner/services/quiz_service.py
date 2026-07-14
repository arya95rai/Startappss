import os
import random
from datetime import datetime

from utils.file_handler import FileHandler
from utils.logger import Logger


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

VOCAB_FILE = os.path.join(
    BASE_DIR,
    "data",
    "vocabulary.csv"
)

PROGRESS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "progress.csv"
)


##################################################
# CREATE PROGRESS FILE
##################################################

def ensure_progress_file():

    if not FileHandler.file_exists(PROGRESS_FILE):

        FileHandler.create_file(
            PROGRESS_FILE,
            [
                "Username",
                "Language",
                "Level",
                "Score",
                "Total",
                "Correct",
                "Wrong",
                "Percentage",
                "Date"
            ]
        )


##################################################
# TAKE QUIZ
##################################################

def take_quiz(username, language, level):

    ensure_progress_file()

    vocabulary = FileHandler.read_csv(VOCAB_FILE)

    if len(vocabulary) <= 1:

        print("\nNo Vocabulary Available.")
        return

    words = []

    for row in vocabulary[1:]:

        if len(row) < 5:
            continue

        if (
            row[2].lower() == language.lower()
            and
            row[4].lower() == level.lower()
        ):

            words.append(row)

    if not words:

        print(
            f"\nNo {language} vocabulary available for {level} level."
        )
        return

    random.shuffle(words)

    questions = words[:min(5, len(words))]

    score = 0

    print("\n" + "=" * 50)
    print("QUIZ")
    print("=" * 50)
    print(f"Language : {language}")
    print(f"Level    : {level}")

    for i, row in enumerate(questions, start=1):

        print("\n--------------------------------")
        print(f"Question {i}/{len(questions)}")
        print("Translate :", row[0])

        answer = input("Answer : ").strip()

        if answer.lower() == row[1].lower():

            print("Correct")

            score += 1

        else:

            print("Wrong")
            print("Correct Answer :", row[1])

    total = len(questions)

    correct = score

    wrong = total - score

    percentage = (score / total) * 100

    if percentage >= 80:

        performance = "Excellent"

    elif percentage >= 60:

        performance = "Good"

    elif percentage >= 40:

        performance = "Average"

    else:

        performance = "Needs Improvement"

    FileHandler.append_csv(

        PROGRESS_FILE,

        [
            username,
            language,
            level,
            score,
            total,
            correct,
            wrong,
            f"{percentage:.2f}",
            datetime.now().strftime("%d-%m-%Y %H:%M")
        ]
    )

    Logger.info(
        f"{username} completed {language} ({level}) quiz."
    )

    print("\n" + "=" * 50)
    print("RESULT")
    print("=" * 50)
    print(f"Score       : {score}/{total}")
    print(f"Correct     : {correct}")
    print(f"Wrong       : {wrong}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Performance : {performance}")
    print("=" * 50)

    input("\nPress Enter to continue...")


##################################################
# VIEW PROGRESS
##################################################

def view_progress(username):

    ensure_progress_file()

    data = FileHandler.read_csv(PROGRESS_FILE)

    found = False

    attempts = 0

    total_score = 0

    total_questions = 0

    print("\n" + "=" * 60)
    print("YOUR QUIZ HISTORY")
    print("=" * 60)

    for row in data[1:]:

        if len(row) < 9:
            continue

        if row[0].lower() == username.lower():

            found = True

            attempts += 1

            score = int(row[3])

            total = int(row[4])

            total_score += score

            total_questions += total

            print("\n--------------------------------")
            print(f"Attempt    : {attempts}")
            print(f"Language   : {row[1]}")
            print(f"Level      : {row[2]}")
            print(f"Score      : {row[3]}/{row[4]}")
            print(f"Percentage : {row[7]}%")
            print(f"Date       : {row[8]}")

    if not found:

        print("\nNo quiz history found.")
        input("\nPress Enter to continue...")
        return

    average = (total_score / total_questions) * 100

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Quiz Attempts : {attempts}")
    print(f"Overall Score : {total_score}/{total_questions}")
    print(f"Average       : {average:.2f}%")
    print("=" * 60)

    input("\nPress Enter to continue...")