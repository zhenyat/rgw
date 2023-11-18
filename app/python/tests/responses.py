#! /usr/bin/env python3

#################################################################
#   Creates table Responses and populates it with faked data
#
#   18.11.2023  Rada Telyukova
#################################################################
from sqlite3 import Error
from termcolor import colored
from faker import Faker
import random
import db

def create(database):
    try:
        conn = db.create_connection(database)

        with conn:
            cur = conn.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Responses (
                    id INTEGER PRIMARY KEY,
                    respondent_id INTEGER,
                    questionnaire_id INTEGER,
                    answer TEXT CHECK(answer IN ('never', 'rarely', 'sometimes', 'regularly')) NOT NULL DEFAULT 'never',
                    FOREIGN KEY(respondent_id) REFERENCES Respondents(id) ON DELETE CASCADE,
                    FOREIGN KEY(questionnaire_id) REFERENCES Questionnaire(id) ON DELETE CASCADE
                ); 
            ''')

            answers = ['never', 'rarely', 'sometimes', 'regularly']

            cur.execute('SELECT id FROM Respondents ORDER BY id')
            respondent_ids = []
            for id, in cur:
                respondent_ids.append(id)

            questionnaire_ids = []
            cur.execute('SELECT id FROM Questionnaire ORDER BY id')
            for id, in cur:
                questionnaire_ids.append(id)

            for respondent_id in respondent_ids:
                for questionnaire_id in questionnaire_ids:

                    answer = random.choice(answers)

                    cur.execute(
                        'INSERT INTO Responses (respondent_id, questionnaire_id, answer) VALUES (?, ?, ?)',
                        (respondent_id, questionnaire_id, answer)
                    )
                    conn.commit() 

        print(colored(f'===== Table "Responses": {cur.lastrowid} records', 'green'))
        conn.close()

    except Error as e:
        print(colored(e, 'red'))