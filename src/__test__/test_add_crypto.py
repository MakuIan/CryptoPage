'''
Unit Test for the add_crypto function.
'''
import sys  # nopep8
sys.path.insert(1, '/Users/maku/Desktop/Projects/CryptoPage/src')  # nopep8
print(sys.path)  # nopep8
from portfolio import Portfolio
from crypto import Crypto
from add_crypto import add_crypto
import sqlite3
import unittest


class TestAddCrypto (unittest.TestCase):
    '''
    Test the add_crypto function.
    '''

    def setUp(self):
        '''
        Set up the database.
        '''
        self.db_path = ':memory:'
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )''')
        c.execute('''CREATE TABLE crypto (
            crypto_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            logo TEXT NOT NULL
        )''')
        conn.commit()
        conn.close()

    def test_add_crypto(self):
        '''
        Test the add_crypto function.
        '''
        crypto = Crypto(1, 'Bitcoin', 'BTC', 10000,
                        'https://bitcoin.org/img/icons/opengraph.png')
        self.portfolio = Portfolio(1)
        self.portfolio.add_crypto(1, 0)

        result = add_crypto(self.db_path, self.portfolio)

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        query = f'SELECT * FROM crypto WHERE crypto_id = 1 and user_id = {self.portfolio.user_id}'
        c.execute(query)
        row = c.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], crypto.id)

        conn.close()

        self.assertTrue(self.portfolio.includes(1))
        self.assertEqual(self.portfolio.cryptos[1].amount, 0)

        self.assertEqual(result, ('Crytpo Added'), self.portfolio)


if __name__ == '__main__':
    unittest.main()
