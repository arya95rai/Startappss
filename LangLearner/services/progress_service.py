import os

from utils.file_handler import FileHandler

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

PROGRESS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "progress.csv"
)


##################################################
# GET USER PROGRESS
##################################################

def get_user_progress(username):

    if not FileHandler.file_exists(PROGRESS_FILE):
        return None

    data = FileHandler.read_csv(PROGRESS_FILE)

    attempts = 0
    total_score = 0
    total_questions = 0
    highest_score = 0

    history = []

    for row in data[1:]:

        if len(row) < 9:
            continue

        if row[0].lower() == username.lower():

            attempts += 1

            score = int(row[3])
            total = int(row[4])

            total_score += score
            total_questions += total

            highest_score = max(
                highest_score,
                score
            )

            history.append({

                "language": row[1],
                "level": row[2],
                "score": score,
                "total": total,
                "percentage": row[7],
                "date": row[8]

            })

    if attempts == 0:
        return None

    average = (
        total_score /
        total_questions
    ) * 100

    if average >= 80:
        current_level = "Advanced"

    elif average >= 60:
        current_level = "Intermediate"

    else:
        current_level = "Beginner"

    return {

        "username": username,
        "attempts": attempts,
        "highest_score": highest_score,
        "average": round(
            average,
            2
        ),
        "level": current_level,
        "history": history

    }


##################################################
# DASHBOARD
##################################################

def show_dashboard(username):

    progress = get_user_progress(username)

    print("\n" + "=" * 60)
    print("YOUR LEARNING DASHBOARD")
    print("=" * 60)

    if progress is None:

        print("\nNo progress available.")
        input("\nPress Enter to continue...")
        return

    print(f"Username       : {progress['username']}")
    print(f"Quiz Attempts  : {progress['attempts']}")
    print(f"Highest Score  : {progress['highest_score']}")
    print(f"Average        : {progress['average']}%")
    print(f"Current Level  : {progress['level']}")

    print("\n========== QUIZ HISTORY ==========")

    for index, item in enumerate(
        progress["history"],
        start=1
    ):

        print("\n--------------------------------")

        print(f"Attempt    : {index}")
        print(f"Language   : {item['language']}")
        print(f"Level      : {item['level']}")
        print(f"Score      : {item['score']}/{item['total']}")
        print(f"Percentage : {item['percentage']}%")
        print(f"Date       : {item['date']}")

    filled = int(progress["average"] // 10)

    print("\nPerformance")

    print(
        "█" * filled +
        "░" * (10 - filled),
        f"{progress['average']}%"
    )

    input("\nPress Enter to continue...")