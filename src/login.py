"""
this module contains the function that handles user login and registration
"""

import hashlib
import sqlite3
from flask import request, redirect, url_for, session, render_template
from user import User


def handle_login(db_path):
    """
    Handle user login and registration.
    """
# create user object
    user = User()
    user.username = request.form['username']
    user.password = request.form['password']
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    # login
    if request.form['submit_button'] == 'login':
        query = f'SELECT username,user_id FROM user WHERE username="{user.username}" AND password="{hashed_password}"'
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(query)
        result = c.fetchone()
        if result:
            user.id = result[1]
            session['id'] = user.id
            session['username'] = user.username
            return redirect(url_for('home', username=user.username, id=str(user.id)))
        else:
            return render_template('login.html', error='Invalid username or password')
    # register
    if request.form['submit_button'] == 'register':
        query = f'SELECT username FROM user WHERE username="{user.username}"'
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(query)
        result = c.fetchone()
        if result:
            return render_template('login.html', error='Username already taken')
        else:
            query = f'INSERT INTO user (username,password) VALUES ("{user.username}","{hashed_password}")'
            c.execute(query)
            conn.commit()
            return redirect(url_for('home', username=user.username, id=str(user.id)))
