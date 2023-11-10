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
from del_crypto import del_crypto
from update_amount import update_amount


def home(db_path, portfolio):
    """
    Render home page.
    """
    if 'home_btn' in request.form:
        if request.form['home_btn'] == 'search_btn':
            return search_crypto(portfolio)
        if request.form['home_btn'] == 'add_crypto_btn':
            return add_crypto(db_path, portfolio)

    if 'portfolio_button' in request.form:
        crypto_id = request.form['portfolio_button']
        return del_crypto(portfolio, int(crypto_id))
    if 'update_btn' in request.form:
        print('hello update')
        crypto_id = request.form['update_btn']
        amount = request.form['amount']
        return update_amount(portfolio, db_path, int(crypto_id), amount)

    return render_template('home.html', id=session['id'], username=session['username'], portfolio=portfolio)
