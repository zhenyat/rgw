######################################################################
#   Creates Test DB table Points and copies data from production DB
#
#   18.11.2023  Rada Telyukova
######################################################################
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
            CREATE TABLE IF NOT EXISTS Points (
                id INTEGER PRIMARY KEY,
                scale_id INTEGER,
                original_points INTEGER NOT NULL,
                male_points INTEGER NOT NULL,
                female_points INTEGER NOT NULL,
                FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
            )
        ''')

        # Get data from the production DB
        cur_production.execute("SELECT * FROM Points;")

        # Populate Testing DB
        for row in cur_production:
            cur_test.execute('''
                    INSERT INTO Points (id, scale_id, original_points, male_points, female_points)
                    VALUES (?, ?, ?, ?, ?)
                ''', row
            )
            conn_test.commit()

        print(colored(f'===== Table "Points": {cur_test.lastrowid} records', 'green'))

        conn_production.close()
        conn_test.close()
        
    except Error as e:
        print(colored(e, 'red'))
