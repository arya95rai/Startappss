import os

from utils.file_handler import FileHandler

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_FOLDER = os.path.join(BASE_DIR, "data")

LANGUAGE_FILE = os.path.join(
    DATA_FOLDER,
    "languages.csv"
)

REQUEST_FILE = os.path.join(
    DATA_FOLDER,
    "language_requests.csv"
)


##################################################
# CREATE FILES
##################################################

def ensure_files():

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not FileHandler.file_exists(LANGUAGE_FILE):

        FileHandler.create_file(
            LANGUAGE_FILE,
            ["Language"]
        )

        FileHandler.append_csv(LANGUAGE_FILE, ["English"])
        FileHandler.append_csv(LANGUAGE_FILE, ["Hindi"])
        FileHandler.append_csv(LANGUAGE_FILE, ["Spanish"])
        FileHandler.append_csv(LANGUAGE_FILE, ["French"])

    if not FileHandler.file_exists(REQUEST_FILE):

        FileHandler.create_file(
            REQUEST_FILE,
            [
                "Username",
                "Language",
                "Status"
            ]
        )


##################################################
# USER SELECT LANGUAGE
##################################################

def select_language(username):

    ensure_files()

    data = FileHandler.read_csv(LANGUAGE_FILE)

    print("\n========== LANGUAGES ==========\n")

    for index, row in enumerate(data[1:], start=1):

        print(f"{index}. {row[0]}")

    print("0. Request New Language")

    choice = input("\nChoice : ").strip()

    if choice == "0":

        language = input(
            "Language Name : "
        ).strip()

        FileHandler.append_csv(

            REQUEST_FILE,

            [
                username,
                language,
                "Pending"
            ]

        )

        print("\nRequest sent to Admin.")

        return None

    try:

        language = data[int(choice)][0]

    except:

        print("\nInvalid Choice.")

        return None

    print("\nSelect Level")

    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    level_choice = input("Choice : ").strip()

    levels = {

        "1": "Beginner",
        "2": "Intermediate",
        "3": "Advanced"

    }

    if level_choice not in levels:

        print("Invalid Level")

        return None

    return (

        language,

        levels[level_choice]

    )


##################################################
# ADMIN ADD LANGUAGE
##################################################

def add_language():

    ensure_files()

    language = input(
        "\nNew Language : "
    ).strip()

    data = FileHandler.read_csv(
        LANGUAGE_FILE
    )

    for row in data[1:]:

        if row[0].lower() == language.lower():

            print("Language already exists.")

            return

    FileHandler.append_csv(

        LANGUAGE_FILE,

        [language]

    )

    print("Language Added Successfully.")


##################################################
# VIEW REQUESTS
##################################################

def view_language_requests():

    ensure_files()

    requests = FileHandler.read_csv(
        REQUEST_FILE
    )

    print("\n========== LANGUAGE REQUESTS ==========\n")

    if len(requests) <= 1:

        print("No Requests.")

        return

    for index, row in enumerate(requests[1:], start=1):

        print(

            f"{index}. "

            f"{row[0]} "

            f"requested "

            f"{row[1]} "

            f"[{row[2]}]"

        )


##################################################
# APPROVE REQUEST
##################################################

def approve_language_request():

    ensure_files()

    requests = FileHandler.read_csv(
        REQUEST_FILE
    )

    if len(requests) <= 1:

        print("No Requests.")

        return

    view_language_requests()

    number = input(
        "\nRequest Number : "
    ).strip()

    try:

        index = int(number)

        language = requests[index][1]

    except:

        print("Invalid Request.")

        return

    languages = FileHandler.read_csv(
        LANGUAGE_FILE
    )

    exists = False

    for row in languages[1:]:

        if row[0].lower() == language.lower():

            exists = True

            break

    if not exists:

        FileHandler.append_csv(

            LANGUAGE_FILE,

            [language]

        )

    requests[index][2] = "Approved"

    FileHandler.write_csv(

        REQUEST_FILE,

        requests

    )

    print("\nLanguage Approved Successfully.")
##################################################
# ADMIN / VOCABULARY LANGUAGE SELECTOR
##################################################

def choose_language():

    ensure_files()

    data = FileHandler.read_csv(
        LANGUAGE_FILE
    )

    print("\n========== SELECT LANGUAGE ==========\n")

    for index, row in enumerate(data[1:], start=1):

        print(f"{index}. {row[0]}")

    choice = input("\nChoice : ").strip()

    try:

        language = data[int(choice)][0]

    except:

        print("\nInvalid Choice.")

        return None

    return language
##################################################
# USER REQUEST NEW LANGUAGE
##################################################

def request_new_language(username):

    ensure_files()

    language = input(
        "\nLanguage Name : "
    ).strip()


    if language == "":
        print("\nLanguage cannot be empty.")
        return


    requests = FileHandler.read_csv(
        REQUEST_FILE
    )


    for row in requests[1:]:

        if (
            row[0].lower() == username.lower()
            and
            row[1].lower() == language.lower()
            and
            row[2].lower() == "pending"
        ):

            print("\nRequest already exists.")

            return


    FileHandler.append_csv(

        REQUEST_FILE,

        [
            username,
            language,
            "Pending"
        ]

    )


    print(
        "\nLanguage request sent successfully."
    )