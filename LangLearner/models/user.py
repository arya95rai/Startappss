class User:

    def __init__(self, username, password, hint, role):
        self.username = username
        self.password = password
        self.hint = hint
        self.role = role


    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"


    def is_admin(self):

        return self.role.lower() == "admin"


    def to_list(self):

        return [
            self.username,
            self.password,
            self.hint,
            self.role
        ]