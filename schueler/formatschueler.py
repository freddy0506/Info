import csv
from ntpath import join

sfile = open("./schueler/schueler.txt", "r")
sformfile = open("./schueler/schuelerFormatet.csv", "w")
sform = csv.writer(sformfile, delimiter=";")

for row in sfile:
    result = []
    if not "Member" in row and not "Profile picture of" in row:
        names = row.split(" ")
        result.append(names[0])
        result.append(" ".join(names[1:])[0:-1])
        sform.writerow(result)
        print(row)