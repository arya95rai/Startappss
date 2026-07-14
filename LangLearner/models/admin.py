from models.user import User


class Admin(User):

    def __init__(
        self,
        username,
        password,
        hint,
        role="admin"
    ):

        super().__init__(
            username,
            password,
            hint,
            role
        )


    def is_admin(self):

        return True



    def get_permissions(self):

        return [
            "view_users",
            "delete_users",
            "view_vocabulary",
            "view_reports",
            "system_statistics"
        ]



    def dashboard(self):

        return """
========== ADMIN DASHBOARD ==========

1. View Users
2. Delete User
3. View Vocabulary
4. View Reports
5. System Statistics
6. Logout

=====================================
"""



    def __str__(self):

        return (
            f"Admin: {self.username}"
        )