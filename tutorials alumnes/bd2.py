import sqlite3

connexio = sqlite3.connect("./BD/tutorialalumnes.db")
cursor = connexio.cursor()
resultat = cursor.execute("SELECT * FROM LlistatAlumnes")
# Es un objecte i no imprimirà res més que un identificador
print(resultat)
# Ara imprimirà el primer resultat del llistat obtingut amb 
# la consulta Select * from llistatAlumnes
llista=resultat.fetchone()
print(llista)
# Teniu en compte que el resultat de fetchone() és una llista i 
# per tant la podem tractar com a tal a tots els efectes.
# Per exemple: llista[1] mostrarà el llinatge2 de la primera fila
print(llista[2])
# i llista[3] mostrarà el nom
print(llista[3])
# Ara obtindrem tots els resultats, excepte la primera fila que ja
# l'havíem obtingut abans
llista=resultat.fetchall()
print(llista)
print(llista[1][2])