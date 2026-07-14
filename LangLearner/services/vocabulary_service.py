import os

from models.vocabulary import Vocabulary

from utils.file_handler import FileHandler
from utils.validators import Validator
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



##################################################
# CREATE FILE
##################################################

def ensure_file():

    if not FileHandler.file_exists(VOCAB_FILE):

        FileHandler.create_file(
            VOCAB_FILE,
            [
                "Word",
                "Translation",
                "Language",
                "Category",
                "Difficulty"
            ]
        )



def add_vocabulary():

    ensure_file()

    from services.language_service import choose_language

    language = choose_language()

    if language is None:

        print("\nNo language selected.")
        return

    print("\n========== ADD VOCABULARY ==========")
    print("Language :", language)

    word = input("Word : ").strip()

    if not Validator.validate_empty(word):

        print("Word cannot be empty.")
        return

    data = FileHandler.read_csv(VOCAB_FILE)

    for row in data[1:]:

        if (
            row[0].lower() == word.lower()
            and
            row[2].lower() == language.lower()
        ):

            print("Word already exists.")
            return

    translation = input("Translation : ").strip()

    category = input("Category : ").strip()

    print("\nDifficulty")

    print("1. Beginner")

    print("2. Intermediate")

    print("3. Advanced")

    choice = input("Choice : ").strip()

    difficulty_map = {

    "1": "Beginner",
    "2": "Intermediate",
    "3": "Advanced"

    }

    if choice not in difficulty_map:

        print("Invalid choice.")
        return

    difficulty = difficulty_map[choice]

    vocab = Vocabulary(

        word,
        translation,
        language,
        category,
        difficulty

    )

    FileHandler.append_csv(

        VOCAB_FILE,
        vocab.to_list()

    )

    Logger.info(
        f"Vocabulary added: {word}"
    )

    print("\nVocabulary Added Successfully.")





#####################################################
# VIEW VOCABULARY
#####################################################

def view_vocabulary(language=None, level=None):

    ensure_file()

    data = FileHandler.read_csv(VOCAB_FILE)

    print("\n========== VOCABULARY ==========")

    if len(data) <= 1:

        print("No Vocabulary Found.")
        return

    found = False

    for row in data[1:]:

        if len(row) < 5:
            continue

        word = row[0]
        translation = row[1]
        word_language = row[2]
        category = row[3]
        difficulty = row[4]

        if language is not None:

            if word_language.lower() != language.lower():
                continue

        if level is not None:

            if difficulty.lower() != level.lower():
                continue

        found = True

        print("\n----------------------------")
        print(f"Word        : {word}")
        print(f"Translation : {translation}")
        print(f"Language    : {word_language}")
        print(f"Category    : {category}")
        print(f"Difficulty  : {difficulty}")

    if not found:

        print("\nNo vocabulary available for this language and level.")





##################################################
# SEARCH VOCABULARY
##################################################

def search_vocabulary():


    ensure_file()



    print(
        """
========== SEARCH ==========

1. Word
2. Language
3. Category
4. Difficulty
"""
    )


    choice = input(
        "Choice : "
    )



    value = input(
        "Search : "
    ).lower()



    data = FileHandler.read_csv(
        VOCAB_FILE
    )


    found = False




    for row in data[1:]:



        match = False



        if choice == "1":

            match = value in row[0].lower()



        elif choice == "2":

            match = value == row[2].lower()



        elif choice == "3":

            match = value == row[3].lower()



        elif choice == "4":

            match = value == row[4].lower()



        if match:


            found = True


            print(
                "\n----------------"
            )


            print(
                f"Word : {row[0]}"
            )


            print(
                f"Meaning : {row[1]}"
            )


            print(
                f"Language : {row[2]}"
            )


            print(
                f"Category : {row[3]}"
            )


            print(
                f"Difficulty : {row[4]}"
            )




    if not found:

        print(
            "No result found."
        )





##################################################
# UPDATE VOCABULARY
##################################################

def update_vocabulary():

    ensure_file()

    from services.language_service import choose_language

    language = choose_language()

    if language is None:

        return

    word = input(
        "\nWord to Update : "
    ).strip()

    data = FileHandler.read_csv(
        VOCAB_FILE
    )

    updated = False

    for row in data[1:]:

        if (
            row[0].lower() == word.lower()
            and
            row[2].lower() == language.lower()
        ):

            updated = True

            print("\nLeave blank to keep old value.")

            translation = input(
                "Translation : "
            )

            category = input(
                "Category : "
            )

            print("""
                  1. Beginner
                  2. Intermediate
                  3. Advanced
                  """)

            choice = input(
                "Level : "
            ).strip()

            level_map = {

                "1": "Easy",
                "2": "Medium",
                "3": "Hard"

            }

            if translation:

                row[1] = translation

            if category:

                row[3] = category

            if choice in level_map:

                row[4] = level_map[choice]

    FileHandler.write_csv(
        VOCAB_FILE,
        data
    )

    if updated:

        Logger.info(
            f"Vocabulary updated: {word}"
        )

        print(
            "\nVocabulary Updated Successfully."
        )

    else:

        print(
            "\nWord not found."
        )





##################################################
# DELETE VOCABULARY
##################################################

def delete_vocabulary():

    ensure_file()

    from services.language_service import choose_language

    language = choose_language()

    if language is None:

        return

    word = input(
        "\nWord to Delete : "
    ).strip()

    data = FileHandler.read_csv(
        VOCAB_FILE
    )

    new_data = [
        data[0]
    ]

    deleted = False

    for row in data[1:]:

        if (
            row[0].lower() == word.lower()
            and
            row[2].lower() == language.lower()
        ):

            deleted = True

            continue

        new_data.append(row)

    FileHandler.write_csv(
        VOCAB_FILE,
        new_data
    )

    if deleted:

        Logger.info(
            f"Vocabulary deleted: {word}"
        )

        print(
            "\nVocabulary Deleted Successfully."
        )

    else:

        print(
            "\nWord not found in this language."
        )