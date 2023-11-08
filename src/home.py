"""
This module contains the Home page.
"""
from flask import session, render_template, request
from crypto import Crypto
# from apikey import CRYPTO_COMPARE_API_KEY as CRYPTO_COMPARE
import sqlite3  # pylint: disable=import-error
from get_crypto_data import get_crypto_data
from add_crypto import add_crypto
from search_crypto import search_crypto
from portfolio import Portfolio
from user import User


def home(db_path):
    """
    Render home page.
    """
    user = User(session['username'], session['password'], session['id'])
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    query = f'SELECT crypto_id, amount FROM portfolio WHERE id = {user.id}'
    c.execute(query)
    data = c.fetchall()
    portfolio = Portfolio(user.id, {})
    for row in data:
        portfolio.add_crypto(row[0], row[1])
    # TODO: add portfolio to add_crypto and search_crypto
    if request.form['home_btn'] == 'search_btn':
        return search_crypto(db_path)
    if request.form['home_btn'] == 'add_crypto_btn':
        return add_crypto(db_path)

    return render_template('home.html', id=session['id'], username=session['username'])
