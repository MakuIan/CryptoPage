class User:
    def __init__(self, username=None, password=None, id=None):
        self._id = id
        self._username = username
        self._password = password

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @id.setter
    def id(self, id):
        self._id = id

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password
