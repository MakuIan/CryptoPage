# This file contains the update_amount function which updates the amount of a
# crypto in the portfolio table.
from flask import render_template, session
import sqlite3


def update_amount(portfolio, db_path, crypto_id, amount):
    """
    Update the amount of a crypto in the portfolio table.
    """
    try:
        amount = float(amount)
        print('update_amount', amount)
        portfolio.update_amount(crypto_id, amount)
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        query = f'UPDATE portfolio SET amount = {amount} WHERE crypto_id = {crypto_id} AND user_id = {portfolio.user_id}'
        c.execute(query)
        conn.commit()
        conn.close()
        return render_template('home.html', id=session['id'], username=session['username'], portfolio=portfolio)
    except ValueError:
        error = 'Invalid Amount'
        return render_template('home.html', id=session['id'], username=session['username'], error=error, portfolio=portfolio)
