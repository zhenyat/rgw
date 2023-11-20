########################################################
#   Creates and populates table Scales with data
#
#   18.11.2023  Rada Telyukova
########################################################
from sqlite3 import Error
from termcolor import colored
import db

def create(database):
    try:
        conn = db.create_connection(database)

        with conn:
            cur = conn.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Scales (
                id INTEGER PRIMARY KEY,
                rus TEXT NOT NULL UNIQUE,
                eng TEXT NOT NULL UNIQUE
                );
            ''')
      
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Конфронтационный копинг', 'Confrontive coping'))
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Дистанцирование', 'Distancing'))
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Самоконтроль', 'Self-controlling'))
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Поиск социальной поддержки', 'Seeking social support'))
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Принятие ответственности', 'Accepting responsibility'))
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Бегство-избегание', 'Escape-avoidance'))
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Планирование решения проблемы', 'Planful problem solving'))
            cur.execute('INSERT INTO Scales (rus, eng) VALUES (?, ?)',
                ('Положительная переоценка', 'Positive reappraisal'))
            conn.commit()

        print(colored(f'===== Table "Scales": {cur.lastrowid} records', 'green'))

        conn.close()

    except Error as e:
        print(colored(e, 'red'))

