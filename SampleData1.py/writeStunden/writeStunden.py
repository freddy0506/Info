from opcode import opname
from mysql import connector
import csv;

sql = "INSERT INTO stunden(vonS, bisS, tag, oft) VALUES (%s, %s, %s, %s);"
data = csv.reader(open("Stunden.csv", "r"), delimiter=";")

conn = connector.connect(host='v-verl.de',
database='schueler',
user='schueler',
password='stundenplan#1Pas')

myCursor = conn.cursor()
first = True
for row in data:
    if not first and len(row) == 5:
        print(row)
        try:
            myCursor.execute(sql,row)
            conn.commit()
        except:
            print("Already There")
    else:
        first = False
   