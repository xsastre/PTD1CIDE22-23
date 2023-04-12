import csv

with open('./BD/LlistatAlumnes.csv', newline='') as arxiu:
    lector = csv.DictReader(arxiu)
    for fila in lector:
        print(fila['Llinatge1']+" "+fila['Nom'])
