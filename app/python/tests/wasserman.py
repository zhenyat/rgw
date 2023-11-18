########################################################
#   Create table Wasserman_u20 and copies data from production DB
#
#   18.11.2023  Rada Telyukova
########################################################
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
            CREATE TABLE IF NOT EXISTS Wasserman_u20 (
                id INTEGER PRIMARY KEY,
                scale_id INTEGER,
                raw_points INTEGER NOT NULL,
                male_points INTEGER NOT NULL,
                female_points INTEGER NOT NULL,
                FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
            )
        ''')

        # Get data from the production DB
        cur_production.execute("SELECT * FROM Wasserman_u20;")

        # Populate Testing DB
        for row in cur_production:
            cur_test.execute('''
                    INSERT INTO Wasserman_u20 (id, scale_id, raw_points, male_points, female_points)
                    VALUES (?, ?, ?, ?, ?)
                ''', row
            )
            conn_test.commit()

        print(
            colored(f'===== Table "Wasserman_u20": {cur_test.lastrowid} records', 'green'))

        conn_production.close()
        conn_test.close()

    except Error as e:
        print(colored(e, 'red'))
