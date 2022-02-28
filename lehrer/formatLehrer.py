import csv
from re import I

# The output syntax will be:
# Nachname;Vorname;Kürzel

lfile = open("./lehrer/lehrer.txt")
lformFile = open("./lehrer/lehrerFormated.csv", "w")
lform = csv.writer(lformFile, delimiter=";")
i=0
for row in lfile:
    #print(row)
    result = []
    if row != "":
        firstName = row.split(",")
        #result.append(i)
        result.append(firstName[0])
        nameShort = firstName[1].split("\t")

        result.append(nameShort[0][1:-1])
        result.append(nameShort[1][:-1])
        lform.writerow(result)
        print(result)
        i+=1
        