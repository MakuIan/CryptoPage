class User:
    def __init__(self, username=None, password=None, user_id=None):
        self._user_id = user_id
        self._username = username
        self._password = password

    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password
