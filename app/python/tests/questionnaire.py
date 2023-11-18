##################################################################
#   Create table Questionnaire and copies data from production DB
#
#   18.11.2023  Rada Telyukova
##################################################################
from sqlite3 import Error
from termcolor import colored
import db


def copy(db_production, db_test):
    try:
        conn_production = db.create_connection(db_production)
        cur_production = conn_production.cursor()

        conn_test = db.create_connection(db_test)
        cur_test = conn_test.cursor()

        cur_test.execute('''
            CREATE TABLE IF NOT EXISTS Questionnaire (
                id INTEGER PRIMARY KEY,
                scale_id INTEGER,
                item TEXT NOT NULL UNIQUE,
                FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
            );
        ''')

        # Get data from the production DB
        cur_production.execute("SELECT * FROM Questionnaire;")

        # Populate Faked DB
        for row in cur_production:
            cur_test.execute(
                'INSERT INTO Questionnaire (id, scale_id, item) VALUES (?, ?, ?)', row)
            conn_test.commit()

        print(colored(f'===== Table "Questionnaire": {cur_test.lastrowid} records', 'green'))

        conn_production.close()
        conn_test.close()

    except Error as e:
        print(colored(e, 'red'))
