import sqlite3
import os


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
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '..', 'data', 'crypto_app.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        query = "SELECT name,symbol,price,logo FROM crypto WHERE crypto_id = ?"
        c.execute(query, (crypto_id,))
        data = c.fetchone()
        name = data[0]
        symbol = data[1]
        price = data[2]
        logo = data[3]
        self.cryptos[crypto_id] = {
            'name': name, 'symbol': symbol, 'price': price, 'logo': logo, 'amount': amount}
        conn.close()

    def del_crypto(self, crypto_id):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '..', 'data', 'crypto_app.db')
        conn = sqlite3.connect(db_path)

        del self.cryptos[crypto_id]
        c = conn.cursor()
        query = f'DELETE FROM portfolio WHERE crypto_id = {crypto_id} AND user_id = {self.user_id}'
        c.execute(query)
        conn.commit()
        conn.close()

    def includes(self, crypto_id):
        return crypto_id in self.cryptos
