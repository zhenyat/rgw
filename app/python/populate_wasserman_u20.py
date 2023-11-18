#! /usr/bin/env python3

####################################################
#   Populates DB table Wasserman_u20
#   with Wasserman under 20 data from CSV file
#
#   17.11.2023  Rada Telyukova
####################################################
import sqlite3

connection = sqlite3.connect('db/rgw.sqlite3')
cursor = connection.cursor()

input_data = open('db/input/wasserman_u20.csv', 'r')

# Extract data from CSV file row by row and insert into DB
for row in input_data:
    cells = []
    cells = row.strip().split(',')
    scale_id = cells.pop(0)
    raw_points = cells.pop(0)
    male_points = cells.pop(0)
    female_points = cells.pop(0)

    cursor.execute('INSERT INTO Wasserman_u20 (scale_id, raw_points, male_points, female_points) VALUES (?, ?, ?, ?)',
                   (scale_id, raw_points, male_points, female_points)
                   )
    connection.commit()

input_data.close()
connection.close()
