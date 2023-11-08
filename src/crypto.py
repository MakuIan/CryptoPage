class Crypto:
    def __init__(self, crypto_id, name, symbol, price, logo):
        self._id = crypto_id
        self.name = name
        self.symbol = symbol
        self.price = price
        self.logo = logo

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def price(self):
        return self._price

    @property
    def logo(self):
        return self._logo

    @id.setter
    def id(self, crypto_id):
        self._id = crypto_id

    @name.setter
    def name(self, name):
        self._name = name

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @price.setter
    def price(self, price):
        self._price = price

    @logo.setter
    def logo(self, logo):
        self._logo = logo
