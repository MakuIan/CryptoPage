from flask import Flask, render_template, request
import sqlite3
import os
from user import User

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', 'data', 'crypto_app.db')

app = Flask(__name__)
# create User object
user = User()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        if request.form['submit_button'] == 'login':
            query = f'SELECT * FROM user WHERE username="{user.username}" AND password="{user.password}"'
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(query)
            result = c.fetchone()
            if result:
                return render_template('home.html', username=user.username)
            else:
                return render_template('login.html', error='Invalid username or password')
        if request.form['submit_button'] == 'register':
            query = f'INSERT INTO user (username, password) VALUES ("{user.username}", "{user.password}")'
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(query)
            conn.commit()
            return render_template('login.html', msg='registerd successfully')

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
    login()
