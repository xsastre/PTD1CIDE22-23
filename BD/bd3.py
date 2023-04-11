import sqlite3


connexio = sqlite3.connect("./BD/tutorialalumnes.db")
# En aquest cas com que no volem obtenir resultats de la BD sinó modificar-la
# aleshores no fa falta el cursor. Utilitzarem directament la connexió
# Aquí el que farem serà modificar la taulaLlistatAlumnes i afegir-li un cap
# Edat. Serà un camp de tipus INTEGER
connexio.execute("ALTER TABLE LlistatAlumnes ADD COLUMN Edat INTEGER")
# Una vegada creat el nou camp podem modificar un registre per afegir-li 
# l'edat. Per exemple al registre que té idAlumne=3
connexio.execute("UPDATE LlistatAlumnes SET Edat=17 WHERE IdAlumne=3")
# Finalment feim el commit per confirmar els canvis
connexio.commit()
connexio.close()