#! /usr/bin/env python3

###############################################################################
#   Calculates original & standard (Wasserman et al.) scores for production DB
#
#   21.11.2023  Rada Telyukova
###############################################################################
from sqlite3 import Error
from termcolor import colored
import db

def main():
    db_production = 'db/rgw.sqlite3'
    conn = db.create_connection(db_production)

    with conn:
        cur = conn.cursor()

        cur.execute("SELECT id, sex FROM Respondents ORDER BY id")
        respondents = cur.fetchall()
        # respondents = cur.fetchmany(5)

        for id, sex in respondents:     ### Respondents Loop
            respondent_id = id

            # Reset Score arrays
            original_score = [0]*9   # Original Scores by Scale (original_score[0] = 'original')
            original_score[0] = 'original'
            standard_score = [0]*9   # Standard Scores by Scale (standard_score[0] = 'standard')
            standard_score[0] = 'standard'

            # Get all responses of the given Responder
            cur.execute(
                '''
                    SELECT questionnaire_id, answer 
                    FROM Responses
                    WHERE respondent_id=?
                ''',
                (respondent_id,)
            )
            responses = cur.fetchall()
            for questionnaire_id, answer in responses:  # Responses Loop

                # Get Scale
                cur.execute("SELECT scale_id FROM Questionnaire WHERE id=?", 
                    (questionnaire_id,)
                )
                for scale_id, in cur.fetchall():
                    match answer:     # Calculate Original score for the Respondent
                        case 'never':
                            original_score[scale_id] += 0
                        case 'rarely':
                            original_score[scale_id] += 1
                        case 'sometimes':
                            original_score[scale_id] += 2
                        case 'regularly':
                            original_score[scale_id] += 3
                        case _:
                            print(colored("Unacceptable 'answer'!", 'red'))
                            exit

            for scale_id in range(1,9):
                cur.execute(
                    '''
                        SELECT male_points, female_points  
                        FROM Points 
                        WHERE scale_id=? AND original_points=?
                    ''',
                    (scale_id, original_score[scale_id])
                )

                wasserman = cur.fetchall()
                for male_points, female_points in wasserman:
                    standard_score[scale_id] = male_points if sex == 'M' else female_points
                
            # print(respondent_id, original_score, standard_score)

            rows = [
                (respondent_id, original_score[0], original_score[1], original_score[2], original_score[3], original_score[4], original_score[5],  original_score[6], original_score[7], original_score[8]),
                (respondent_id, standard_score[0], standard_score[1], standard_score[2], standard_score[3], standard_score[4], standard_score[5],  standard_score[6], standard_score[7], standard_score[8])
            ]
            # print(rows)

            try:
                cur.executemany(
                    '''
                        INSERT INTO Scores (respondent_id, kind, v1, v2, v3, v4, v5, v6, v7, v8) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    rows
                )
                conn.commit()

            except Error as e:
                print(colored(e, 'red'))

    print(colored(f'===== Table "Scores": {cur.lastrowid} records', 'green'))

if __name__ == '__main__':
    main()
