from random import choice
import sqlite3
import os
from unittest import result
from art import *
from click import style
from tabulate import tabulate
con = sqlite3.connect("schueler.db")
cur = con.cursor()


class root():
    path = "/"

    def __init__(self, intro, optionName, pathName="/", type="") -> None:
        self.optionName = optionName
        self.pathName = pathName
        self.intro = intro
        self.nextRoots = []
        self.type = type

    def printHead(self):
        os.system("clear")
        tprint("SQL", font="alpha")
        print("Mit diesem Terminal kann man mit der Datenbank kommunizieren.")


    def getOptionName(self):
        return self.optionName
    
    def setPath(self, frontPath):
        self.path = frontPath + self.pathName + "/"

    def addRoot(self, other):
        other.setPath(self.path)
        self.nextRoots.append(other)
    
    def askOption(self):
        
        #print(len(self.nextRoots))
        if len(self.nextRoots) < 1:
            return (self.pathName, self.type)
        else:
            self.printHead()
            print("\n")
            print(self.intro)
            print()
            i = 0
            while i<len(self.nextRoots):
                print(str(i) + ". " + self.nextRoots[i].getOptionName())
                i+=1
            print("\n99. Zurück")

            choiceValid = False
            while(not choiceValid):
                choice = input(self.path + ": ")
                if(not choice == "99" and (not choice.isdecimal() or int(choice) >= len(self.nextRoots)+1 or int(choice) < 0)):
                    print("Invalid Choice")
                else:
                    choiceValid = True
                    if(int(choice) == 99):
                        return (["back"])
                    else:
                        choice = self.nextRoots[int(choice)].askOption()
                        print (choice[0])
                        if choice[0] == "back":
                            #print("selfAsk")
                            return self.askOption()
                        else:
                            return choice

mainRoot = root("Sie haben diese Optionen: ", "")

selectTable = root("Welche Tabelle soll aus gegeben werden? ", "Gesamte Tabellen ausgeben" , "selectTable")
selectTable.addRoot(root("", "Schüler", "schueler", "selectT"))
selectTable.addRoot(root("", "Kurse", "kurse", "selectT"))
selectTable.addRoot(root("", "Stunden Zeiten", "stunden", "selectT"))
selectTable.addRoot(root("", "Lehrer", "lehrer", "selectT"))
selectTable.addRoot(root("", "Stunden-Kurse Beziehung", "stundenKurs", "selectT"))
selectTable.addRoot(root("", "Schüler-Kurse Beziehung", "schuelerKurs", "selectT"))

showStundenplan = root("Von wem wollen sie den Stundenplan sehen? ", "Individueller Stundenplan", "stundenplan")
cur.execute("SELECT * FROM schueler;")
for s in cur.fetchall():
    #print(s)
    showStundenplan.addRoot(root("",s[1] + " " + s[2], s[1] + "+" + s[2], "showSt"))


mainRoot.addRoot(selectTable)
mainRoot.addRoot(showStundenplan)

def selectStundeplan(name):
    cur.execute("""
    SELECT kurse.name, stunden.tag, stunden.vonS, stunden.bisS
    FROM schueler 
        JOIN schuelerKurs
        ON schuelerKurs.SID = schueler.SID
        JOIN kurse 
        ON schuelerKurs.name = kurse.name AND schuelerKurs.stufe = kurse.stufe
        JOIN stundenKurs
        ON kurse.name = stundenKurs.name
        JOIN stunden
        ON stundenKurs.StId = stunden.StId
    WHERE schueler.vorname = '""" + name[0] + """' AND schueler.nachname = '""" + name[1] + """' ORDER BY  stunden.tag;
    """)

    print(tabulate(cur.fetchall(), headers=["Kurs", "Wochentag", "Stunden Beginn", "Stunden Ende"] , tablefmt="pretty"))


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

def selectTabelle(name):
    cur.execute("SELECT * FROM " + name + ";")
    print(tabulate(cur.fetchall(), tablefmt="pretty"))


# Ask the User what to do
choice = mainRoot.askOption()
#print(choice)

if choice[0] == "back":
    print("Quitting...")
    quit()
elif choice[1] == "selectT":
    selectTabelle(choice[0])
elif choice[1] == "showSt":
    selectStundeplan(choice[0].split("+"))