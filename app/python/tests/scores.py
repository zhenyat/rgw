#! /usr/bin/env python3

########################################################
#   Calculates raw & std (Wasserman et al.) scores
#
#   20.11.2023  Rada Telyukova
########################################################
from sqlite3 import Error
from termcolor import colored
import db

def main():
    db_test = 'db/rgw_test.sqlite3'
    conn = db.create_connection(db_test)

    with conn:
        cur = conn.cursor()

        cur.execute("SELECT id, sex FROM Respondents ORDER BY id LIMIT 1")
        respondents = cur.fetchall()
        # respondents = cur.fetchmany(5)

        for id, sex in respondents:     ### Respondents Loop

            raw_score = [0]*9   # Raw score by Scale (raw_score[0] - not used)
            score = [0]*9       # Scores by Scale (scores[0] - not used)
            respondent_id = id

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
                    match answer:     # Calculate Raw score for the Respondent
                        case 'never':
                            raw_score[scale_id] += 0
                        case 'rarely':
                            raw_score[scale_id] += 1
                        case 'sometimes':
                            raw_score[scale_id] += 2
                        case 'regularly':
                            raw_score[scale_id] += 3
                        case _:
                            print(colored("Unacceptable 'answer'!", 'red'))
                            exit

            for scale_id in range(1,9):
                cur.execute(
                    '''
                        SELECT male_points, female_points  
                        FROM Wasserman_u20 
                        WHERE scale_id=? AND raw_points=?
                    ''',
                    (scale_id, raw_score[scale_id])
                )

                wasserman = cur.fetchall()
                for male_points, female_points in wasserman:
                    score[scale_id] = male_points if sex == 'M' else female_points
                
            try:
                cur.execute(
                    '''
                        INSERT INTO Scores (respondent_id, v0, v1, v2, v3, v4, v5, v6, v7, v8) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (respondent_id, score[0], score[1], score[2], score[3], score[4], score[5], score[6], score[7], score[8])
                )
                conn.commit()

            except Error as e:
                print(colored(e, 'red'))

if __name__ == '__main__':
    main()
