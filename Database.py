import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stufftoplot(unix REAL, datestamp REAL, keyword REAL, value REAL)')



s = "(unix, datestamp, keyword, value)"



unix = 10
date = 50
keyword = 12
value1 = 1000
value2 = 2000

lov1 = [unix,date,keyword,value1]
lov2 = [unix,date,keyword,value2]

lov = lov1,lov2

def dynamic_data_entry(listofheaders,listofvalues):
    c.execute("INSERT INTO stufftoplot" + listofheaders + "VALUES (?, ?, ?, ?)",
              ([listofvalues[i]for i in range(len(listofvalues))]))
    conn.commit()


def read_from_db():
    c.execute("SELECT * FROM stufftoplot WHERE value > 2")
    for row in c.fetchall():
        print (row)


def del_and_update():
    c.execute("SELECT * FROM stufftoplot")
    [print(row) for row in c.fetchall()]

    c.execute("UPDATE stufftoplot SET value = 99 WHERE value = 6.0")
    conn.commit()

    c.execute("SELECT * FROM stufftoplot")
    [print(row) for row in c.fetchall()]


print (s)
print (lov1)



create_table()
"""for i in range(len(lov)):
    dynamic_data_entry(s,lov[i])"""
#read_from_db()
# graph_date()

c.close()
conn.close()

