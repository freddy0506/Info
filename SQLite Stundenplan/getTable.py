import sqlite3
con = sqlite3.connect("schueler.db")
cur = con.cursor()

while True:
    cur.execute("SELECT * FROM " + input("Table: ") + ";")

    print(cur.fetchall())