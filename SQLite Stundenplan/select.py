import imp
from importlib.resources import path
import sqlite3
import os
from art import *
from click import option, style
con = sqlite3.connect("schueler.db")
cur = con.cursor()

os.system("clear")

class root():
    nextRoots = []
    optionName = ""
    path = "/"

    def __init__(self, optionName, path) -> None:
        self.optionName = optionName
        self.path = path
    
    def getOptionName(self):
        return self.optionName

    def addRoot(self, root):      
        self.nextRoots.append(root)
    
    def askOption(self):
        if len(self.nextRoots) < 1:
            return self.path
        else:
            i = 1
            while i<len(self.nextRoots)-1:
                print(str(i) + ". " + self.nextRoots[i].getOptionName())
                i+=1
            print(str(i+1) + ". zurück")

            input(path)

tprint("SQL", font="alpha")

print("Mit diesem Terminal kann man mit der Datenbank kommunizieren. Es folgen die möglchen Befehle:")

print("   1. Tabellen ausgeben")
print("   2. Stundenplan")
print()
print("Um einen Befehl auszuwählen geben sie die entsprechende Nummer ein")
input("/: ")
def selectStundeplan(name):
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
    WHERE schueler.vorname = '""" + name + """' ORDER BY  stunden.tag;
    """)
    
    for row in cur.fetchall():
        print(" ".join(str(i) for i in row))


def selectKursTeilnehmer(name):
    cur.execute("""
    SELECT schueler.vorname, schueler.nachname
    FROM schueler
        JOIN schuelerKurs
        ON schueler.SID = schuelerKurs.SID
        JOIN kurse
        ON schuelerKurs.name = kurse.name AND schuelerKurs.stufe = kurse.stufe
    WHERE kurse.name = """ +  name + """;
    """)
    
    for row in cur.fetchall():
        print(" ".join(str(i) for i in row))