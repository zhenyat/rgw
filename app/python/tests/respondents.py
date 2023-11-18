#! /usr/bin/env python3

#################################################################
#   Creates table Respondents and populates it with faked data
#
#   18.11.2023  Rada Telyukova
#################################################################
from sqlite3 import Error
from termcolor import colored
from faker import Faker
import db

def create(database):
    try:
        conn = db.create_connection(database)

        with conn:
            cur = conn.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Respondents (
                    id INTEGER PRIMARY KEY,
                    school_id INTEGER,
                    email TEXT UNIQUE,
                    sex TEXT CHECK(sex IN ('F', 'M')) NOT NULL DEFAULT 'F',
                    age INTEGER NOT NULL DEFAULT 15,
                    form INTEGER CHECK(form IN (9, 11)) NOT NULL DEFAULT 9,
                    FOREIGN KEY(school_id) REFERENCES Schools(id) ON DELETE CASCADE
                );
            ''')

            # Generate faked data to populate the 'Respondents'
            faker = Faker('ru_RU')

            cur.execute("SELECT id FROM Schools where nick='dummy'")
            for id, in cur:
                school_id = id

            for form in (9, 11):
                age = 15 if form == 9 else 17
                for i in range(50):
                    p = faker.profile()
                    sex = p['sex']
                    email = p['mail']

                    cur.execute(
                        'INSERT INTO Respondents (school_id, email, sex, age, form) VALUES (?, ?, ?, ?, ?)',
                        (school_id, email, sex, age, form)
                    )
                    conn.commit()

        print(colored(f'===== Table "Respondents": {cur.lastrowid} records', 'green'))
        conn.close()

    except Error as e:
        print(colored(e, 'red'))
