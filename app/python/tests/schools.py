################################################################
#   Creates and populates Test DB table Schools with faked data
#
#   18.11.2023  Rada Telyukova
################################################################
from sqlite3 import Error
from termcolor import colored
import db

def create(database):
    try:
        conn = db.create_connection(database)

        with conn:
            cur = conn.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Schools (
                id INTEGER PRIMARY KEY,
                nick TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL
                );
            ''')

            cur.execute(
                'INSERT INTO Schools (nick, title) VALUES (?, ?)',
                ('dummy',  'Dummy school for testing')
            )

            conn.commit()

        print(colored(f'===== Table "Schools": {cur.lastrowid} records', 'green'))
        conn.close()

    except Error as e:
        print(colored(e, 'red'))
