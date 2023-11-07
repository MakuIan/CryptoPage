import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', '..', 'data', 'crypto_app.db')
conn = sqlite3.connect(db_path)

c = conn.cursor()

c.execute('''Alter TABLE crypto ADD COLUMN logo TEXT''')

conn.commit()

conn.close()
