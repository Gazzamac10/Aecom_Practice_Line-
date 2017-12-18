import os
import sqlite3

Path = "C:\\Users\mccarthyg\PycharmProjects\Aecom_Practice_Line-\\new_ACM_S_SBM_SP_UEA.txt"

f = open(Path, 'r')
a = f.readlines()

headingstring = a[0].strip().split(",")
headings = []
for item in headingstring:
    headings.append(item.split("##")[0].replace(" ","_"))

headingcontainers = []
for item in headings:
    headingcontainers.append(item + " TEXT")

tableheadingscont  = "(" + ", ".join(headingcontainers) +")"
tableheadings  = "(" + ", ".join(headings) +")"

data = a[1:]
datalines = [data[i].strip().split(",")for i in range(len(data))]

markstring = ",".join(["?" for i in range(len(headings))])
marks = "("+markstring+")"




conn = sqlite3.connect('RevitFamilyDB.db')
c = conn.cursor()


def create_table(listofheaderscont):
    c.execute("CREATE TABLE IF NOT EXISTS new_ACM_S_SBM_SP_UEA" + listofheaderscont + "")


def dynamic_data_entry(listofheaders,listofvalues):
    c.execute("INSERT INTO new_ACM_S_SBM_SP_UEA" + listofheaders + "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?)",
              ([listofvalues[i]for i in range(len(listofvalues))]))
    conn.commit()


create_table(tableheadingscont)

for i in range(len(datalines)):
    dynamic_data_entry(tableheadings,datalines[i])

c.close()
conn.close()
