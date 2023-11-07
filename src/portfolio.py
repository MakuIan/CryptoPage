class Portfolio:
    def __init__(self, id, user, crypto, amount):
        self.id = id
        self.user = user
        self.crypto = crypto
        self.amount = amount

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def crypto(self):
        return self._crypto

    @crypto.setter
    def crypto(self, value):
        self._crypto = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
