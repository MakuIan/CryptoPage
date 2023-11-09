"""
This module contains the Flask application for the Crypto App.
The application handles user login and registration,
and provides access to various cryptocurrency data.
"""
import logging
import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, session
from login import handle_login
from home import home as home_page
from portfolio import Portfolio
from user import User
import sqlite3


current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', 'data', 'crypto_app.db')

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Handle user login and registration.

    If the request method is POST, the function checks whether the user is logging in or registering.
    If the user is logging in, the function checks the username and password against the database.
    If the user is registering, the function checks whether the username is already taken.
    """
    if request.method == 'POST':
        logging.debug('POST request received')
        return handle_login(db_path)
    else:
        return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    Render home page.
    """
    if 'id' in session:
        user = User(session['username'], session['id'])
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        query = f'SELECT crypto_id, amount FROM portfolio WHERE id = {user.id}'
        c.execute(query)
        data = c.fetchall()
        portfolio = Portfolio(session['id'])
        for row in data:
            portfolio.add_crypto(row[0], row[1])
        if request.method == 'POST':
            return home_page(db_path, portfolio)
        else:
            return render_template('home.html', id=session['id'], username=session['username'], portfolio=portfolio)
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
