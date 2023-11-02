from flask import Flask, render_template, request
import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    print('POST')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('login.html', username=username, password=password)
    else:
        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
    login()
