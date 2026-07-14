class Quiz:


    def __init__(
        self,
        question,
        answer,
        language="General",
        difficulty="Easy"
    ):

        self.question = question
        self.answer = answer
        self.language = language
        self.difficulty = difficulty
        self.score = 0



    def check_answer(
        self,
        user_answer
    ):

        if (
            user_answer.strip().lower()
            ==
            self.answer.strip().lower()
        ):

            self.score = 1

            return True


        return False



    def __str__(self):

        return (
            f"Question : {self.question}\n"
            f"Language : {self.language}\n"
            f"Difficulty : {self.difficulty}"
        )



    def to_list(self):

        return [
            self.question,
            self.answer,
            self.language,
            self.difficulty
        ]