#! /usr/bin/env python3

##########
#   Just for testing...
##########

from sqlite3 import Error
from termcolor import colored
from faker import Faker
from enum import Enum
from faker_enum import EnumProvider
import random
import db

conn_test = db.create_connection('db/rgw_test.sqlite3')
cur_test = conn_test.cursor()

# The results are returned as a list of tuples.
# Each tuple corresponds to a row in the database that we accessed.
# Dealing with data this way is painful.
cur_test.execute("SELECT * FROM Scores where respondent_id=3")
results = cur_test.fetchall()
print(results)

exit()

# Array to / from DB
original_score = ['original', 14, 9, 8, 11, 8, 9, 7, 6]
standard_score = ['standard', 67, 52, 31, 51, 51, 47, 33, 34]

rows = [
    (3, original_score[0], original_score[1], original_score[2], original_score[3],
     original_score[4], original_score[5], original_score[6], original_score[7], original_score[8]),
    (3, standard_score[0], standard_score[1], standard_score[2], standard_score[3],
     standard_score[4], standard_score[5], standard_score[6], standard_score[7], standard_score[8])
]
print('rows to be inserted: ', rows)
row = (1, original_score[0], original_score[1], original_score[2], original_score[3],
       original_score[4], original_score[5], original_score[6], original_score[7], original_score[8]),

cur_test.executemany(
    '''
        INSERT INTO Scores (respondent_id, kind, v1, v2, v3, v4, v5, v6, v7, v8) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    rows
)
conn_test.commit()

cur_test.execute(
    "SELECT * FROM Scores where respondent_id=3 AND kind='standard'")
for row in cur_test:
    print('--- selected row as tuple: ', row)
    for i in range(len(row)):
        print(i, row[i])

    standard_scores = list(row)   # tuple to list
    print('Final - standard_scores: ', standard_scores)

# Array to / from DB (end)


cur_test.execute("SELECT id FROM Schools where nick='dummy'")
# the trailing comma after result unpacks the element from
# the single-element tuple
for result, in cur_test:
    print(result)  # --> 1

cur_test.execute("SELECT id FROM Schools where nick='dummy'")
for result in cur_test:
    print(result)  # --> (1,)

cur_test.execute("SELECT id FROM Schools where nick='dummy'")
for id, in cur_test:
    school_id = id
print(school_id)


fake = Faker('ru_RU')
fake.add_provider(EnumProvider)


class Color(Enum):
    RED = 1
    green = 2
    BLUE = 3


print(fake.enum(Color))
print(fake.enum(Color))
print(type(fake.enum(Color)))


class Foo(Enum):
    a = 0
    b = 1
    c = 2


print(Foo)
print(random.choice(list(Foo)))
print(random.choice(list(Foo)))
print(random.choice(list(Foo)))

answers = ['never', 'rarely', 'sometimes', 'regularly']
print(random.choice(answers))
print(random.choice(answers))
print(random.choice(answers))

cur_test.execute('SELECT id FROM Respondents ORDER BY id')
respondent_ids = []
for id, in cur_test:
    respondent_ids.append(id)
print(respondent_ids)

questionnaire_ids = []
cur_test.execute('SELECT id FROM Questionnaire ORDER BY id')
for id, in cur_test:
    questionnaire_ids.append(id)
print(questionnaire_ids)

for id in respondent_ids:
    print(id)
