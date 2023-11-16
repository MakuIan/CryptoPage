import unittest
import sqlite3
import sys  # nopep8
sys.path.insert(1, '/Users/maku/Desktop/Projects/CryptoPage/src')  # nopep8
print(sys.path)  # nopep8
from portfolio import Portfolio


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.db_path = ':memory:'
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        c.execute('''CREATE TABLE portfolio (
            portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            crypto_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (user_id),
            FOREIGN KEY (crypto_id) REFERENCES crypto (crypto_id)
        )''')
        conn.commit()
        c.execute(
            '''INSERT INTO user (username, password) VALUES ('test', 'test')''')
        c.execute('''INSERT INTO crypto(crypto_id, name, symbol, price, logo)
            VALUES (1, 'Bitcoin', 'BTC', 10000, 'https://bitcoin.org/img/icons/opengraph.png')''')
        c.execute(
            '''INSERT INTO portfolio(user_id, crypto_id, amount) VALUES (1, 1, 0)''')
        conn.commit()
        conn.close()

    def test_add(self):
        portfolio = Portfolio(1)

        # add crypto to portfolio
        crypto_id = 1
        amount = 1
        portfolio.add_crypto(crypto_id, amount)

        added_crypto = portfolio.cryptos[crypto_id]

        self.assertEqual(added_crypto['name'], 'Bitcoin')
        self.assertEqual(added_crypto['symbol'], 'BTC')
        self.assertIsInstance(added_crypto['price'], float)
        self.assertEqual(added_crypto['amount'], 1)

    def test_del(self):
        portfolio = Portfolio(1)

        # add crypto to portfolio
        crypto_id = 1
        amount = 1
        portfolio.add_crypto(crypto_id, amount)

        # delete crypto from portfolio
        portfolio.del_crypto(crypto_id)

        self.assertNotIn(crypto_id, portfolio.cryptos, 'test_del failed')

        print('test_del passed')

    def test_calc_value(self):
        portfolio = Portfolio(1)

        # add crypto to portfolio
        crypto_id = 1
        amount = 1
        portfolio.add_crypto(crypto_id, amount)

        # calculate value of crypto in portfolio
        portfolio.calc_value(crypto_id)

        self.assertIsInstance(portfolio.cryptos[crypto_id]['value'], float)

    def test_update_amount(self):
        portfolio = Portfolio(1)

        # add crypto to portfolio
        crypto_id = 1
        amount = 10
        portfolio.add_crypto(crypto_id, amount)

        portfolio.update_amount(crypto_id, amount)

        self.assertEqual(portfolio.cryptos[crypto_id]['amount'], 10)

        print('test_calc_value passed')


if __name__ == '__main__':
    unittest.main()
