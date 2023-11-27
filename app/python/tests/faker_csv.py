#! /usr/bin/env python3

###############
#   Generates faked data and imports to csv
###############
import sqlite3
# from sqlite3 import Error
# import pandas as pd
# from termcolor import colored
from faker import Faker
import random

faker = Faker('ru_RU')

# forms = [9, 11]
# school_nicks = ['dummy', 'empty']
answers = ['никогда', 'редко', 'иногда', 'часто']

conn = sqlite3.connect("db/rgw_test.sqlite3")

with conn:
    cur = conn.cursor()


    for n in range(5):
        row = []
        # timestamp: "17.11.2023 15:05:11"
        timestamp = faker.date_time_this_month().strftime("%d.%m.%Y %H:%M:%S")
        row.append(timestamp)

        profile = faker.profile()
        row.append(profile['mail'])
        row.append(profile['sex'])

        # form = random.choice(forms)
        # if form == 9: age = 15
        # else:         age = 17

        # school_nick = random.choice(school_nicks)
        # 'SELECT  id FROM Schools WHERE nick=?', school_nick

        for i in range(50):
            row.append(random.choice(answers))
        print("\n",n,row) 

# DataFrame.to_csv(filename, sep=',', index=False, encoding='utf-8')