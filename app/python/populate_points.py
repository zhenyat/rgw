#! /usr/bin/env python3

####################################################
#   Populates DB table Points
#   with Wasserman under 20 data from CSV file
#
#   17.11.2023  Rada Telyukova
####################################################
import sqlite3
from termcolor import colored

connection = sqlite3.connect('db/rgw.sqlite3')
cursor = connection.cursor()

input_data = open('db/csv/points.csv', 'r')

# Extract data from CSV file row by row and insert into DB
for row in input_data:
    cells = []
    cells = row.strip().split(',')
    scale_id = cells.pop(0)
    original_points = cells.pop(0)
    male_points = cells.pop(0)
    female_points = cells.pop(0)

    cursor.execute('INSERT INTO Points (scale_id, original_points, male_points, female_points) VALUES (?, ?, ?, ?)',
                   (scale_id, original_points, male_points, female_points)
                   )
    connection.commit()

print(colored(f'===== Table "Points": {cursor.lastrowid} records inserted', 'green'))

input_data.close()
connection.close()
