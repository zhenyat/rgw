##########################################################
#   Creates a database connection to the SQLite database
#   specified by the 'db_file'
#
#   Returns Connection object or None
#
#   18.11.2023  Rada Telyukova
##########################################################
import sqlite3
from sqlite3 import Error
from termcolor import colored

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(colored(e, 'red'))

    return connection
