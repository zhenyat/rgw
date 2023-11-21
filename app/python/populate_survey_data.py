#! /usr/bin/env python3

####################################################
#   Populates DB tables Respondents & Responses
#   with collected survey data from CSV file
#
#   17.11.2023  Rada Telyukova
####################################################
import sqlite3

connection = sqlite3.connect('db/rgw.sqlite3')
cursor = connection.cursor()

input_data = open('db/csv/google_numbers.csv', 'r')

# Extract data from CSV file row by row
for row in input_data:
    cells = []
    cells = row.strip().split(';')
    school_id = int(cells.pop(0))
    form = int(cells.pop(0))

    # Populate data into 'Respondents'
    email = cells.pop(0)

    # Translate sex
    sex = 'M' if (cells.pop(0) == 'Мужской') else 'F'
    # Emulate age while it is not in Questionnaire
    age = 15 if form == 9 else 17

    cursor.execute('INSERT INTO Respondents (school_id, email, sex, age, form) VALUES (?, ?, ?, ?, ?)',
        (school_id, email, sex, age, form)
    )
    connection.commit()

    current_respondent_id = cursor.lastrowid   # Current (last) Respondent

    # Populate data into 'Responses'
    answers = []
    for i in range(len(cells)):
        questionnaire_id = i + 1
        # answer = cells.pop(0)
        match cells.pop(0):
            case 'никогда':
                answer = 'never'
            case 'редко':
                answer = 'rarely'
            case 'иногда':
                answer = 'sometimes'
            case 'часто':
                answer = 'regularly'
            case _:
                exit()

        cursor.execute('INSERT INTO Responses (respondent_id, questionnaire_id, answer) VALUES (?, ?, ?)',
                       (current_respondent_id, questionnaire_id, answer)
                       )
        connection.commit()

input_data.close()
connection.close()
