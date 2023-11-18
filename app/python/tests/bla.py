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

cur_test.execute("SELECT id FROM Schools where nick='dummy'")
# the trailing comma after result unpacks the element from 
# the single-element tuple
for result, in cur_test: 
    print(result) #--> 1

cur_test.execute("SELECT id FROM Schools where nick='dummy'")
for result in cur_test:
    print(result)   #--> (1,)

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