import sqlite3
import os
from get_crypto_data import get_crypto_data_by_id as get_crypto_data


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
        '''Add a crypto to the portfolio.'''
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
        '''Delete a crypto from the portfolio.'''
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '..', 'data', 'crypto_app.db')
        conn = sqlite3.connect(db_path)

        del self.cryptos[crypto_id]
        c = conn.cursor()
        query = f'DELETE FROM portfolio WHERE crypto_id = {crypto_id} AND user_id = {self.user_id}'
        c.execute(query)
        conn.commit()
        conn.close()

    def calc_value(self, crypto_id):
        '''Calculate the value of a crypto in the portfolio.'''
        self.cryptos[crypto_id]['value'] = self.cryptos[crypto_id]['amount'] * \
            self.cryptos[crypto_id]['price']

    def update_amount(self, crypto_id, amount):
        '''Update the amount of a crypto in the portfolio.'''
        self.cryptos[crypto_id]['amount'] = amount
        self.cryptos[crypto_id]['value'] = amount * \
            self.cryptos[crypto_id]['price']

    def includes(self, crypto_id):
        '''Return True if the portfolio includes the crypto.'''
        return crypto_id in self.cryptos

    def update_crypto_price(self, crypto_id):
        '''Update the price of a crypto in the portfolio.'''
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, '..', 'data', 'crypto_app.db')
        conn = sqlite3.connect(db_path)

        c = conn.cursor()
        crypto = get_crypto_data(crypto_id)
        self.cryptos[crypto_id]['price'] = crypto.price
        self.cryptos[crypto_id]['value'] = crypto.price * \
            self.cryptos[crypto_id]['amount']
        query = 'UPDATE crypto SET price = ? WHERE crypto_id = ?'
        c.execute(query, (crypto.price, crypto_id))
        conn.commit()
        conn.close()
