import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('TestingDatabase.db')
c = conn.cursor()

def read_from_db():
    c.execute("SELECT * FROM outfromGH")
    test = []
    for row in c.fetchall():
        test.append(row)
    return test


for item in read_from_db():
    print (item[0])