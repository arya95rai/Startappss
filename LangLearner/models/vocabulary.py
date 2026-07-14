class Vocabulary:


    def __init__(
        self,
        word,
        translation,
        language,
        category,
        difficulty
    ):

        self.word = word
        self.translation = translation
        self.language = language
        self.category = category
        self.difficulty = difficulty



    def __str__(self):

        return (
            f"Word        : {self.word}\n"
            f"Translation : {self.translation}\n"
            f"Language    : {self.language}\n"
            f"Category    : {self.category}\n"
            f"Difficulty  : {self.difficulty}"
        )



    def to_list(self):

        return [
            self.word,
            self.translation,
            self.language,
            self.category,
            self.difficulty
        ]