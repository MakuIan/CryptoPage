import os
import sqlite3
import hashlib

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', '..', 'data', 'crypto_app.db')

conn = sqlite3.connect(db_path)

c = conn.cursor()

new_password = hashlib.sha256('aa'.encode()).hexdigest()

query = 'UPDATE user SET password = ? WHERE user_id = ?'

c.execute(query, (new_password, 1))

conn.commit()

conn.close()
