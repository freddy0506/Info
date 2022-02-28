import sqlite3
con = sqlite3.connect("schueler.db")
cur = con.cursor()

while True:
    cur.execute("""
    SELECT schueler.vorname, kurse.name, stunden.tag, stunden.vonS, stunden.bisS
    FROM schueler 
        JOIN schuelerKurs
        ON schuelerKurs.SID = schueler.SID
        JOIN kurse 
        ON schuelerKurs.name = kurse.name AND schuelerKurs.stufe = kurse.stufe
        JOIN stundenKurs
        ON kurse.name = stundenKurs.name
        JOIN stunden
        ON stundenKurs.StId = stunden.StId
    WHERE schueler.vorname = '""" + input("Name: ") + """' ORDER BY  stunden.tag;
    """)
    for row in cur.fetchall():
        print(" ".join(str(i) for i in row))