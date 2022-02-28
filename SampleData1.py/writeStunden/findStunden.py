from opcode import opname
from mysql import connector
import csv;

sql = "SELECT * FROM stunden WHERE tag = %s AND vonS = %s AND bisS = %s;"
data = csv.reader(open("Stunden.csv", "r"), delimiter=";")

conn = connector.connect(host='v-verl.de',
database='schueler',
user='schueler',
password='stundenplan#1Pas')

myCursor = conn.cursor()
while(True):
    myCursor.execute(sql, (input("Tag: "), input("Von Stunde: "), input("Bis Stunde: ")))
    #conn.commit()
    for result in myCursor.fetchall():
        print("ID = " + str(result[0])  + "   " + str(result[4]))
        print("")