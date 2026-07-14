import os

from utils.file_handler import FileHandler
from utils.logger import Logger

from services.progress_service import (
    get_user_progress
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_FOLDER = os.path.join(
    BASE_DIR,
    "data"
)

USERS_FILE = os.path.join(
    DATA_FOLDER,
    "users.csv"
)

VOCAB_FILE = os.path.join(
    DATA_FOLDER,
    "vocabulary.csv"
)


##################################################
# COUNT VOCABULARY
##################################################

def count_vocabulary():

    if not FileHandler.file_exists(VOCAB_FILE):
        return 0

    data = FileHandler.read_csv(VOCAB_FILE)

    return max(len(data) - 1, 0)


##################################################
# USER ROLE
##################################################

def get_user_role(username):

    if not FileHandler.file_exists(USERS_FILE):
        return "Unknown"

    users = FileHandler.read_csv(
        USERS_FILE
    )

    for row in users[1:]:

        if row[0].lower() == username.lower():

            return row[3]

    return "Unknown"


##################################################
# USER REPORT
##################################################

def generate_report(username):

    print("\n" + "=" * 60)
    print("USER REPORT")
    print("=" * 60)

    role = get_user_role(username)

    progress = get_user_progress(username)

    print(f"Username : {username}")
    print(f"Role     : {role}")
    print(f"Vocabulary Available : {count_vocabulary()}")

    if progress is None:

        print("\nNo quiz history available.")

        input("\nPress Enter to continue...")
        return

    print("\n========== PERFORMANCE ==========")

    print(f"Quiz Attempts : {progress['attempts']}")
    print(f"Highest Score : {progress['highest_score']}")
    print(f"Average       : {progress['average']}%")
    print(f"Current Level : {progress['level']}")

    print("\n========== HISTORY ==========")

    for attempt in progress["history"]:

        print("--------------------------------")

        print(
            f"Language   : {attempt['language']}"
        )

        print(
            f"Level      : {attempt['level']}"
        )

        print(
            f"Score      : {attempt['score']}/{attempt['total']}"
        )

        print(
            f"Percentage : {attempt['percentage']}%"
        )

        print(
            f"Date       : {attempt['date']}"
        )

    Logger.info(
        f"Report generated for {username}"
    )

    input("\nPress Enter to continue...")


##################################################
# ADMIN REPORT
##################################################

def generate_all_reports():

    users = FileHandler.read_csv(
        USERS_FILE
    )

    if len(users) <= 1:

        print("No users found.")
        return

    for row in users[1:]:

        generate_report(
            row[0]
        )