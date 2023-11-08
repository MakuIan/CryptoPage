import sqlite3
import pickle
from flask import session, render_template, request
from crypto import Crypto


def add_crypto(db_path, portfolio):
    '''Add crypto to database.'''

    data = session['crypto']
    crypto = pickle.loads(data)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    query = f'SELECT crypto_id FROM crypto WHERE crypto_id = {crypto.id}'
    c.execute(query)
    result = c.fetchone()
    # adding crpto to crypto table
    if result is None:
        query = 'INSERT INTO crypto (crypto_id, name, symbol,price,logo) VALUES (?, ?, ?, ?, ?)'
        c.execute(query, (crypto.id, crypto.name,
                  crypto.symbol, crypto.price, crypto.logo))
        conn.commit()
    else:
        query = "UPDATE crypto SET price = ? WHERE crypto_id = ?"
        c.execute(query, (crypto.price, crypto.id))
        conn.commit()

    # adding crypto to portfolio table
    if portfolio.includes(crypto.id):
        msg = 'Crypto Already Added'
        return render_template('home.html', id=session['id'], username=session['username'], msg=msg, portfolio=portfolio)
    query = 'INSERT INTO portfolio (crypto_id,user_id,amount) VALUES (?, ?,?)'
    c.execute(query, (crypto.id, session['id'], 0))
    conn.commit()
    portfolio.add_crypto(crypto.id, 0)
    conn.close()
    msg = 'Crypto Added'
    return render_template('home.html', id=session['id'], username=session['username'], msg=msg, portfolio=portfolio)
