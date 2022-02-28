from opcode import opname
from mysql import connector
import csv;

sql = "INSERT INTO stundenKurs(name, stufe, StId) VALUES (%s, %s, %s);"
data = csv.reader(open("StundenKurs.csv", "r"), delimiter=";")

conn = connector.connect(host='v-verl.de',
database='schueler',
user='schueler',
password='stundenplan#1Pas')

myCursor = conn.cursor()
first = True
for row in data:
    if not first and len(row) == 3:
        print(row)
        try:
            myCursor.execute(sql,row)
            conn.commit()
        except:
            print("Already There")
    else:
        first = False
   