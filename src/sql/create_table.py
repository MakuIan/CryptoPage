import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', '..', 'data', 'crypto_app.db')
conn = sqlite3.connect(db_path)

c = conn.cursor()

c.execute('''CREATE TABLE portfolio(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            crypto_id INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (crypto_id) REFERENCES cryptos(id)
)''')

conn.commit()

conn.close()
