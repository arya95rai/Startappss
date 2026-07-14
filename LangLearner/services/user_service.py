import os

from utils.file_handler import FileHandler

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

USERS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "users.csv"
)


def update_learning_preference(username, language, level):

    data = FileHandler.read_csv(USERS_FILE)

    if not data:
        return

    header = data[0]

    if "PreferredLanguage" not in header:
        header.extend([
            "PreferredLanguage",
            "Level"
        ])

    for row in data[1:]:

        while len(row) < len(header):
            row.append("")

        if row[0].lower() == username.lower():

            row[-2] = language
            row[-1] = level

    FileHandler.write_csv(
        USERS_FILE,
        data
    )