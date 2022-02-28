import csv

while True:
    lformFile = open("./lehrerFormated.csv", "r")
    lform = csv.reader(lformFile, delimiter=";")

    st = input("Short: ")
    for row in lform:
        if row[2] == st:
            print(row)