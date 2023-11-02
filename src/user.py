class User:
    def __init__(self, username, password, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password

    @property
    def user_id(self):
        return self.user_id

    @property
    def username(self):
        return self.username

    @property
    def password(self):
        return self.password
