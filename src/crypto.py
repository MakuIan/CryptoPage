class crypto:
    def __init__(self, crypto_id, name, symbol, price):
        self.crypto_id = crypto_id
        self.name = name
        self.symbol = symbol
        self.price = price

    def __repr__(self):
        return f'crypto({self.crypto_id}, {self.name}, {self.symbol}, {self.price})'

    def __str__(self):
        return f'crypto({self.crypto_id}, {self.name}, {self.symbol}, {self.price})'

    @property
    def crypto_id(self):
        return self._crypto_id

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def price(self):
        return self._price

    @crypto_id.setter
    def crypto_id(self, crypto_id):
        self._crypto_id = crypto_id

    @name.setter
    def name(self, name):
        self._name = name

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @price.setter
    def price(self, price):
        self._price = price
