class Portfolio:

    def __init__(self, user_id):
        self.user_id = user_id
        self.cryptos = {}

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    # methods

    def add_crypto(self, crypto_id, amount):
        self.cryptos[crypto_id] = amount

    def del_crypto(self, crypto_id):
        del self.cryptos[crypto_id]

    def includes(self, crypto_id):
        return crypto_id in self.cryptos
