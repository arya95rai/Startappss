class Validator:


    @staticmethod
    def validate_empty(value):

        if value is None:
            return False

        if value.strip() == "":
            return False

        return True



    @staticmethod
    def validate_password(password):

        # minimum 4 characters
        if len(password) < 4:
            return False

        return True



    @staticmethod
    def validate_role(role):

        roles = [
            "user",
            "admin"
        ]

        return role.lower() in roles



    @staticmethod
    def validate_difficulty(difficulty):

        levels = [
            "easy",
            "medium",
            "hard"
        ]

        return difficulty.lower() in levels



    @staticmethod
    def validate_score(score):

        try:

            score = int(score)

            if score < 0:
                return False

            return True


        except ValueError:

            return False



    @staticmethod
    def validate_duplicate(existing_data, value):

        for row in existing_data:

            if row[0].lower() == value.lower():

                return True


        return False