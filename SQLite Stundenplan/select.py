from email import header
import sqlite3
import os
import sys
from art import *
from tabulate import tabulate
con = sqlite3.connect("schueler.db")
cur = con.cursor()

# Diese Klasse nutzte ich um das "Tree-Interface" darzustellen
class root():
    path = "/"

    def __init__(self, intro, optionName, pathName="/", type="", title="Main") -> None:
        self.optionName = optionName
        self.pathName = pathName
        self.intro = intro
        self.nextRoots = []
        self.type = type
        self.title = title

    def printHead(self):
        if sys.platform == "linux" or sys.platform == "linux2":
            os.system("clear")
        else:
            os.system("cls")
            
        tprint(self.title, font="big")
        print("Mit diesem Terminal kann man mit der Datenbank kommunizieren. Geben Sie die Nummer der gewünschten Option ein.")


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
                        #print (choice[0])
                        if choice[0] == "back":
                            #print("selfAsk")
                            return self.askOption()
                        else:
                            return choice

mainRoot = root("Sie haben diese Optionen: ", "")

# Die Baumstruktur für das Ausgeben der verschiedenen Tabellen wird definiert
selectTable = root("Welche Tabelle soll aus gegeben werden? ", "Gesamte Tabellen ausgeben" , "selectTable", "", "Tabellen")
selectTable.addRoot(root("", "Schüler", "schueler", "selectT"))
selectTable.addRoot(root("", "Kurse", "kurse", "selectT"))
selectTable.addRoot(root("", "Stunden Zeiten", "stunden", "selectT"))
selectTable.addRoot(root("", "Lehrer", "lehrer", "selectT"))
selectTable.addRoot(root("", "Stunden-Kurse Beziehung", "stundenKurs", "selectT"))
selectTable.addRoot(root("", "Schüler-Kurse Beziehung", "schuelerKurs", "selectT"))

# Die Baustruktur der Option "Individualpläne" wird erstellt. Dabei werden alle Schüler hinzugefügt 
showStundenplan = root("Von wem wollen Sie den Stundenplan sehen? ", "Individueller Stundenplan", "stundenplan", "", "Stundenplan")
cur.execute("SELECT * FROM schueler;")
for s in cur.fetchall():
    showStundenplan.addRoot(root("",s[1] + " " + s[2], s[1] + "+" + s[2], "showSt"))

# Hier wird die Baumstruktur der option "Kurslisten" definiert. Alle Kurse werden angezeigt
kursListen = root("Von welchem Kurs wollen Sie die Kursliste sehen?", "Kurslisten", "kursListen", "kuLists", "Kurse")
cur.execute("SELECT * FROM Kurse;")
for k in cur.fetchall():
    #print(k)
    kursListen.addRoot(root("",k[2] + " " + k[3] +" (" + str(k[4]) + ")", k[0] + "+" + k[1], "kuLists"))

# Für die das Abrufen der Zeiten wird eine ähnliche Struktur wie bei "Kurslisten" erstellt
kursZeiten = root("Hier können die Zeiten der Kurse abgerufen werden", "Kurszeiten", "kursZeiten", "", "Zeiten")
cur.execute("SELECT * FROM Kurse;")
for k in cur.fetchall():
    #print(k)
    kursZeiten.addRoot(root("",k[2] + " " + k[3] +" (" + str(k[4]) + ")", k[0] + "+" + k[1], "kuZeiten"))

# Die Unterbäume werden zum Hauptbaum hinzugefügt
mainRoot.addRoot(showStundenplan)
mainRoot.addRoot(selectTable)
mainRoot.addRoot(kursListen)
mainRoot.addRoot(kursZeiten)

# Bestimmten Stundenplan anzeigen. (name = [<Vorname>, <Nachname>])
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

# Eine bestimmte Kursliste ausgeben
def selectKursTeilnehmer(name):
    cur.execute("""
    SELECT schueler.vorname, schueler.nachname
    FROM schueler
        JOIN schuelerKurs
        ON schueler.SID = schuelerKurs.SID
        JOIN kurse
        ON schuelerKurs.name = kurse.name AND schuelerKurs.stufe = kurse.stufe
    WHERE kurse.name = '""" +  name[0] + """' AND kurse.stufe = '""" +  name[1] + """';
    """)
    
    print(tabulate(cur.fetchall(), headers=["Vorname", "Nachname"] , tablefmt="pretty"))

# Die Zeiten der eines bestimmten Kurses ausgeben
def stundenZeiten(name):
    print(name[0] + ":")
    cur.execute("""
    SELECT stunden.tag, stunden.vonS, stunden.bisS
    FROM kurse
        JOIN stundenKurs
        ON kurse.name = stundenKurs.name
        JOIN stunden
        ON stundenKurs.StId = stunden.StId
    WHERE kurse.name = '""" +  name[0] + """' AND kurse.stufe = '""" +  name[1] + """';
    """)
    
    print(tabulate(cur.fetchall(), headers=["Wochentag", "Von", "Bis"] , tablefmt="pretty"))

# Einen Tabelle ausgeben
def selectTabelle(name):
    cur.execute("SELECT * FROM " + name + ";")
    h = []
    for n in cur.description:
        h.append(n[0])
    print(tabulate(cur.fetchall(), headers=h, tablefmt="pretty"))


while True:
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
    elif choice[1] == "kuLists":
        selectKursTeilnehmer(choice[0].split("+"))
    elif choice[1] == "kuZeiten":
        stundenZeiten(choice[0].split("+"))

    input("\n\n Weitersuchen? [enter]")