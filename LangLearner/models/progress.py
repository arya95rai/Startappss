class Progress:


    def __init__(
        self,
        username,
        language,
        score,
        total_questions,
        percentage,
        date
    ):

        self.username = username
        self.language = language
        self.score = score
        self.total_questions = total_questions
        self.percentage = percentage
        self.date = date



    def calculate_percentage(self):

        if self.total_questions == 0:

            return 0


        return (
            self.score /
            self.total_questions
        ) * 100



    def get_level(self):

        percentage = self.calculate_percentage()


        if percentage >= 80:

            return "Advanced"


        elif percentage >= 60:

            return "Intermediate"


        else:

            return "Beginner"




    def __str__(self):

        return (
            f"User       : {self.username}\n"
            f"Language   : {self.language}\n"
            f"Score      : {self.score}/{self.total_questions}\n"
            f"Percentage : {self.percentage}%\n"
            f"Level      : {self.get_level()}"
        )



    def to_list(self):

        return [
            self.username,
            self.language,
            self.score,
            self.total_questions,
            f"{self.percentage:.2f}%",
            self.date
        ]