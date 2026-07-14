import services.auth_service as auth

from utils.logger import Logger



##################################################
# PAUSE FUNCTION
##################################################

def pause():

    input(
        "\nPress Enter to continue..."
    )





##################################################
# MAIN MENU
##################################################

def show_main_menu():

    print("\n" + "="*60)

    print(
        "                 🌍 LangLearner"
    )

    print("="*60)


    print(
        """
1. Login
2. Register
3. Forgot Password
4. Exit
"""
    )


    print("="*60)






##################################################
# MAIN FUNCTION
##################################################

def main():

    Logger.info(
        "LangLearner application started"
    )



    while True:


        show_main_menu()



        choice = input(
            "Enter Choice : "
        ).strip()



        try:



            if choice == "1":

                auth.login()

                pause()



            elif choice == "2":

                auth.register()

                pause()



            elif choice == "3":

                auth.forgot_password()

                pause()



            elif choice == "4":


                Logger.info(
                    "Application closed"
                )


                print(
                    "\nThank you for using LangLearner."
                )


                break




            else:


                print(
                    "\nInvalid Choice."
                )

                pause()




        except Exception as e:


            Logger.exception(
                str(e)
            )


            print(
                "\nSomething went wrong."
            )


            pause()





##################################################
# START
##################################################

if __name__ == "__main__":

    main()