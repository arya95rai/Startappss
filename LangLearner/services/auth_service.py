import os
import hashlib
from datetime import datetime

from models.user import User
from models.admin import Admin

from utils.file_handler import FileHandler
from utils.validators import Validator
from utils.logger import Logger

from services.language_service import (
    choose_language,
    request_new_language
)

from services.user_service import (
    update_learning_preference
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


LOGIN_ATTEMPT_FILE = os.path.join(
    DATA_FOLDER,
    "login_attempts.csv"
)


ADMIN_SECRET = "admin123"


MAX_LOGIN_ATTEMPTS = 3





##################################################
# FILE INITIALIZATION
##################################################

def ensure_files():

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


    if not FileHandler.file_exists(USERS_FILE):

        FileHandler.create_file(
            USERS_FILE,
            [
                "Username",
                "Password",
                "Hint",
                "Role",
                "Joined"
            ]
        )


    if not FileHandler.file_exists(LOGIN_ATTEMPT_FILE):

        FileHandler.create_file(
            LOGIN_ATTEMPT_FILE,
            [
                "Username",
                "Attempts",
                "Status"
            ]
        )





##################################################
# PASSWORD HASHING
##################################################

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()





##################################################
# REGISTER
##################################################

def register():

    ensure_files()


    print("\n" + "="*50)
    print("REGISTER")
    print("="*50)



    username = input(
        "Username : "
    ).strip()



    if not Validator.validate_empty(username):

        print(
            "Username cannot be empty."
        )

        return




    users = FileHandler.read_csv(
        USERS_FILE
    )



    for row in users[1:]:

        if row[0].lower() == username.lower():

            print(
                "Username already exists."
            )

            return





    password = input(
        "Password : "
    ).strip()



    if not Validator.validate_password(password):

        print(
            "Password must contain minimum 4 characters."
        )

        return





    confirm = input(
        "Confirm Password : "
    ).strip()



    if password != confirm:

        print(
            "Passwords do not match."
        )

        return





    hint = input(
        "Password Hint : "
    ).strip()





    print(
        """
1. User
2. Admin
"""
    )


    role_choice = input(
        "Role : "
    ).strip()





    joined = datetime.now().strftime(
        "%d-%m-%Y"
    )





    if role_choice == "1":


        user = User(
            username,
            hash_password(password),
            hint,
            "user"
        )


        data = user.to_list()

        data.append(joined)




    elif role_choice == "2":


        key = input(
            "Enter Admin Secret Key : "
        ).strip()



        if key != ADMIN_SECRET:

            print(
                "Invalid Admin Secret Key."
            )

            return




        admin = Admin(
            username,
            hash_password(password),
            hint
        )


        data = admin.to_list()

        data.append(joined)





    else:

        print(
            "Invalid Role."
        )

        return






    FileHandler.append_csv(
        USERS_FILE,
        data
    )



    Logger.info(
        f"New user registered: {username}"
    )



    print(
        "\nRegistration Successful."
    )
##################################################
# LOGIN ATTEMPTS
##################################################

def get_attempt(username):

    data = FileHandler.read_csv(
        LOGIN_ATTEMPT_FILE
    )


    for row in data[1:]:

        if row[0].lower() == username.lower():

            return int(row[1])


    return 0





def update_attempt(username):

    data = FileHandler.read_csv(
        LOGIN_ATTEMPT_FILE
    )


    found = False


    for row in data[1:]:

        if row[0].lower() == username.lower():

            row[1] = str(
                int(row[1]) + 1
            )

            row[2] = "Failed"

            found = True



    if not found:

        data.append(
            [
                username,
                "1",
                "Failed"
            ]
        )



    FileHandler.write_csv(
        LOGIN_ATTEMPT_FILE,
        data
    )





def reset_attempt(username):

    data = FileHandler.read_csv(
        LOGIN_ATTEMPT_FILE
    )


    for row in data[1:]:

        if row[0].lower() == username.lower():

            row[1] = "0"
            row[2] = "Success"



    FileHandler.write_csv(
        LOGIN_ATTEMPT_FILE,
        data
    )





##################################################
# LOGIN
##################################################

def login():

    ensure_files()


    print("\n" + "="*50)
    print("LOGIN")
    print("="*50)



    username = input(
        "Username : "
    ).strip()


    if get_attempt(username) >= MAX_LOGIN_ATTEMPTS:

        print(
            "Account temporarily blocked."
        )

        return




    password = input(
        "Password : "
    ).strip()



    hashed = hash_password(
        password
    )



    users = FileHandler.read_csv(
        USERS_FILE
    )



    for row in users[1:]:


        if (
            row[0].lower() == username.lower()
            and row[1] == hashed
        ):


            reset_attempt(username)



            Logger.info(
                f"Login successful: {username}"
            )


            print(
                "\nLogin Successful."
            )



            if row[3].lower() == "admin":


                admin = Admin(
                    row[0],
                    row[1],
                    row[2],
                    row[3]
                )


                admin_dashboard(admin)



            else:


                user = User(
                    row[0],
                    row[1],
                    row[2],
                    row[3]
                )


                user_dashboard(user)



            return





    update_attempt(username)



    Logger.warning(
        f"Failed login: {username}"
    )


    print(
        "\nInvalid Username or Password."
    )


    print(
        """
1. Try Again
2. Forgot Password
3. Back
"""
    )


    choice = input(
        "Choice : "
    )



    if choice == "1":

        login()


    elif choice == "2":

        forgot_password()





##################################################
# FORGOT PASSWORD
##################################################

def forgot_password():

    ensure_files()


    username = input(
        "Username : "
    ).strip()



    users = FileHandler.read_csv(
        USERS_FILE
    )



    for row in users[1:]:


        if row[0].lower() == username.lower():



            print(
                "Password Hint:",
                row[2]
            )



            new_password = input(
                "New Password : "
            ).strip()



            if not Validator.validate_password(
                new_password
            ):

                print(
                    "Password too short."
                )

                return



            confirm = input(
                "Confirm Password : "
            ).strip()



            if new_password != confirm:

                print(
                    "Passwords do not match."
                )

                return



            row[1] = hash_password(
                new_password
            )


            FileHandler.write_csv(
                USERS_FILE,
                users
            )


            Logger.info(
                f"Password changed: {username}"
            )


            print(
                "Password Updated."
            )

            return



    print(
        "Username not found."
    )







####################################################
# USER DASHBOARD
####################################################

def user_dashboard(user):

    language = choose_language()

    if language is None:

        request = input(
            "\nLanguage not available.\nDo you want to request it? (y/n): "
        ).strip().lower()

        if request == "y":
            request_new_language(user.username)

        return

    print("\nChoose Current Level")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    level_choice = input("Choice : ").strip()

    level_map = {
    "1": "Beginner",
    "2": "Intermediate",
    "3": "Advanced"
}

    if level_choice not in level_map:

        print("Invalid Level.")
        return

    level = level_map[level_choice]

    update_learning_preference(
        user.username,
        language,
        level
    )

    while True:

        print("\n========== USER DASHBOARD ==========")
        print(f"Welcome {user.username}")
        print(f"Language : {language}")
        print(f"Level    : {level}")

        print("""
1. View Vocabulary
2. Search Vocabulary
3. Take Quiz
4. View Progress
5. Generate Report
6. Change Language
7. Logout
""")

        choice = input("Choice : ").strip()

        if choice == "1":

            from services.vocabulary_service import view_vocabulary

            view_vocabulary(language, level)

        elif choice == "2":

            from services.vocabulary_service import search_vocabulary

            search_vocabulary()

        elif choice == "3":

            from services.quiz_service import take_quiz

            take_quiz(
                user.username,
                language,
                level
            )

        elif choice == "4":

            from services.progress_service import show_dashboard

            show_dashboard(user.username)

        elif choice == "5":

            from services.report_service import generate_report

            generate_report(user.username)

        elif choice == "6":

            return user_dashboard(user)

        elif choice == "7":

            print("Logged Out Successfully.")
            break

        else:

            print("Invalid Choice.")





##################################################
# ADMIN DASHBOARD
##################################################

def admin_dashboard(admin):

    while True:

        print("\n" + "=" * 60)
        print("               ADMIN DASHBOARD")
        print("=" * 60)

        print("1. Add New Language")
        print("2. View Available Languages")
        print("3. View Language Requests")
        print("4. Approve Language Request")
        print("5. Add Vocabulary")
        print("6. Update Vocabulary")
        print("7. Delete Vocabulary")
        print("8. View Users")
        print("9. Delete User")
        print("10. Generate All Reports")
        print("11. System Statistics")
        print("12. Logout")

        choice = input("\nChoice : ").strip()

        if choice == "1":

            from services.language_service import add_language

            add_language()

        elif choice == "2":

                from services.language_service import view_languages

                view_languages()

        elif choice == "3":

                from services.language_service import view_language_requests

                view_language_requests()

        elif choice == "4":

                from services.language_service import approve_language_request

                approve_language_request()

        elif choice == "5":

                from services.vocabulary_service import add_vocabulary

                add_vocabulary()

        elif choice == "6":

                from services.vocabulary_service import update_vocabulary

                update_vocabulary()

        elif choice == "7":

                from services.vocabulary_service import delete_vocabulary

                delete_vocabulary()

        elif choice == "8":

                view_users()

        elif choice == "9":

                delete_user()

        elif choice == "10":

                from services.report_service import generate_all_reports

                generate_all_reports()

        elif choice == "11":

                system_statistics()

        elif choice == "12":

                print("\nAdmin Logged Out Successfully.")

                break

        else:

                print("\nInvalid Choice.")





##################################################
# ADMIN FUNCTIONS
##################################################

def view_users():

    users = FileHandler.read_csv(
        USERS_FILE
    )


    print(
        "\n========== USERS =========="
    )


    for row in users[1:]:

        print(
            f"{row[0]} | {row[3]} | Joined: {row[4]}"
        )





def delete_user():

    username = input(
        "Username to delete : "
    )



    users = FileHandler.read_csv(
        USERS_FILE
    )


    new_data = [
        users[0]
    ]


    deleted = False



    for row in users[1:]:


        if row[0].lower() == username.lower():

            deleted = True
            continue


        new_data.append(row)



    FileHandler.write_csv(
        USERS_FILE,
        new_data
    )


    if deleted:

        Logger.info(
            f"User deleted: {username}"
        )

        print(
            "User Deleted."
        )

    else:

        print(
            "User not found."
        )






def system_statistics():


    users = len(
        FileHandler.read_csv(
            USERS_FILE
        )
    ) - 1



    vocab_file = os.path.join(
        DATA_FOLDER,
        "vocabulary.csv"
    )



    progress_file = os.path.join(
        DATA_FOLDER,
        "progress.csv"
    )



    vocab = len(
        FileHandler.read_csv(
            vocab_file
        )
    ) - 1



    quizzes = len(
        FileHandler.read_csv(
            progress_file
        )
    ) - 1



    print(
        """
========== SYSTEM STATISTICS ==========
"""
    )


    print(
        "Users:",
        max(users,0)
    )


    print(
        "Vocabulary:",
        max(vocab,0)
    )


    print(
        "Quiz Attempts:",
        max(quizzes,0)
    )