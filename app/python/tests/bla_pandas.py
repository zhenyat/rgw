#! /usr/bin/env python3

##########
#   Just for testing SQLite - Python - Pandas
##########

import sqlite3
from sqlite3 import Error
# import numpy as np
import pandas as pd
from termcolor import colored
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

con = sqlite3.connect("db/rgw_test.sqlite3")
df = pd.read_sql_query(
    "SELECT v1,v2,v3,v4,v5,v6,v7,v8 from Scores WHERE kind='standard'", con)
print(df.head())
print(df.info)
print(df["v1"].mean(), df["v1"].std())
print(df.shape)

df.hist()
plt.savefig('app/python/tests/standard_hist.pdf')

df = pd.read_sql_query(
    "SELECT v1,v2,v3,v4,v5,v6,v7,v8 from Scores WHERE kind='original'", con)
df.hist()
plt.savefig('app/python/tests/original_hist.pdf')
exit()

engine = create_engine("sqlite:///db/rgw_test.sqlite3")
connection = engine.connect()
df = pd.read_sql_table('Respondents', con=connection)
print(df.head())
print(df["v1"].mean())
connection.close()

#####################################################
# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("db/rgw_test.sqlite3")
df = pd.read_sql_query("SELECT * from Scores;", con)
# df = pd.read_sql("SELECT * from Scores", con)
print(df)
print(df.info())

# Verify that result of SQL query is stored in the dataframe
# print(df.head(10))
# print(df.tail(10))

con.close()
