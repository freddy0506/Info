import sqlite3
import csv;


con = sqlite3.connect("schueler.db")

cur = con.cursor()

# Create Tables
cur.executescript(open("setup.sql").read())

# Insert Lehrer
sql = "INSERT INTO lehrer(nachname, vorname, short) VALUES (?, ?, ?);"
data = csv.reader(open("lehrerFormated.csv", "r"), delimiter=";")

first = True
for row in data:
    if(not first):
        print(row)
        try:
            cur.execute(sql,row)
        except:
            print("Already There")
    else:
        first = False
con.commit()

# Insert Schueler
sql = "INSERT INTO schueler(SID, vorname, nachname, stufe) VALUES (?, ?, ?, ?);"
data = csv.reader(open("Schueler.csv", "r"), delimiter=";")

first = True
for row in data:
    if not first and len(row) == 4:
        print(row)
        try:
            cur.execute(sql,row)
        except:
            print("Already There")
    else:
        first = False
con.commit()

# Insert Stunden
sql = "INSERT INTO stunden(StId,vonS, bisS, tag, oft) VALUES (?, ?, ?, ?, ?);"
data = csv.reader(open("Stunden.csv", "r"), delimiter=";")

first = True
for row in data:
    if not first and len(row) == 5:
        print(row)
        try:
            cur.execute(sql,row)
        except:
            print("Already There")
    else:
        first = False
con.commit()

# Insert Kurse
sql = "INSERT INTO kurse(stufe, name, fach, art, nummer, lShort, raum) VALUES (?, ?, ?, ?, ?, ?, ?);"
data = csv.reader(open("Kurse.csv", "r"), delimiter=";")

first = True
for row in data:
    if not first and len(row) == 7:
        print(row)
        try:
            cur.execute(sql,row)
        except:
            print("Already There")
    else:
        first = False
con.commit()

# Insert Stunden-Kurs verbindungen
sql = "INSERT INTO stundenKurs(name, stufe, StId) VALUES (?, ?, ?);"
data = csv.reader(open("StundenKurs.csv", "r"), delimiter=";")

first = True
for row in data:
    if not first and len(row) == 3:
        print(row)
        try:
            cur.execute(sql,row)
        except:
            print("Already There")
    else:
        first = False
con.commit()

# Insert Schueler-Kurs verbindungen
sql = "INSERT INTO schuelerKurs(SID, name, stufe) VALUES (?, ?, ?);"
data = csv.reader(open("schuelerKurs.csv", "r"), delimiter=";")

first = True
for row in data:
    if(not first):
        print(row)
        try:
            cur.execute(sql,row)
        except:
            print("Already There")
    else:
        first = False
con.commit()

con.close()