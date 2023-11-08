import sqlite3
import pickle
from flask import session, render_template, request
from crypto import Crypto


def add_crypto(db_path):

    data = session['crypto']
    crypto = pickle.loads(data)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    query = f'SELECT crypto_id FROM crypto WHERE crypto_id = {crypto.id}'
    c.execute(query)
    result = c.fetchone()
    if result is None:
        query = f'INSERT INTO crypto (crypto_id, name, symbol,price,logo) VALUES (?, ?, ?, ?, ?)")'
        c.execute(query, (crypto.id, crypto.name,
                  crypto.symbol, crypto.price, crypto.logo))
        conn.commit()
        msg = 'Crypto Added'
    else:
        query = f"UPDATE crypto SET price = ? WHERE crypto_id = ?"
        c.execute(query, (crypto.price, crypto.id))
        conn.commit()
        msg = 'Crypto Already Added'
    conn.close()
    return render_template('home.html', id=session['id'], username=session['username'], msg=msg)
