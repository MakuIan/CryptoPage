from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
from user import User
import hashlib
import secrets

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', 'data', 'crypto_app.db')

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# create User object
user = User()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        hashed_password = hashlib.sha256(
            user.password.encode()).hexdigest()
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
                return render_template('login.html', error='Username already exists')
            query = f'INSERT INTO user (username, password) VALUES ("{user.username}", "{hashed_password}")'
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(query)
            conn.commit()
            return render_template('login.html', msg='registerd successfully')

    return render_template('login.html')


@app.route('/home')
def home():
    if 'id' in session:
        return render_template('home.html', id=session['id'], username=session['username'])
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
