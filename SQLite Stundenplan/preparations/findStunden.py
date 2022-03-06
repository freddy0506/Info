import sqlite3

con = sqlite3.connect("../schueler.db")
cur = con.cursor()

while(True):
    cur.execute("SELECT * FROM stunden WHERE tag = " + input("Tag: ") + " AND vonS = " + input("Von Stunde: ") + " AND bisS = " + input("Bis Stunde: ") + ";")
    #conn.commit()
    for result in cur.fetchall():
        print("ID = " + str(result[0])  + "   " + str(result[4]))
        print("")