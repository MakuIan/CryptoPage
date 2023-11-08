class Portfolio:
    cryptos = {}

    def __init__(self, user_id, cryptos):
        self.user_id = user_id
        self.cryptos = cryptos

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def cryptos(self):
        return self.cryptos

    @cryptos.setter
    def cryptos(self, value):
        self.cryptos = value

    # methods

    def add_crypto(self, crypto_id, amount):
        self.cryptos[crypto_id] = amount

    def del_crypto(self, crypto_id):
        del self.cryptos[crypto_id]
