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


@app.route('/home')
def home():
    """
    Render home page.
    """
    if 'id' in session:
        return render_template('home.html', id=session['id'], username=session['username'])
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
