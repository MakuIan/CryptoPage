import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', '..', 'data', 'user.db')

conn = sqlite3.connect(db_path)

c = conn.cursor()

# c.execute('''CREATE TABLE users(
#           user_id integer primary key autoincrement,
#           username text,
#           password text
# )''')
# c.execute('ALTER TABLE users RENAME TO user')

conn.commit()

conn.close()
