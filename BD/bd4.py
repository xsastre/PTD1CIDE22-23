import sqlite3
from Alumne import Alumne
connexio = sqlite3.connect("./BD/tutorialalumnes.db")

alumneNou=Alumne()
alumneNou.Edat=20
alumneNou.Nom="Pep"
alumneNou.Llinatge1="Calafell"
alumneNou.Llinatge2="Verdera"

connexio.execute("INSERT INTO LlistatAlumnes(Edat,Nom,Llinatge1,Llinatge2) values ("+str(alumneNou.Edat)+",'"+\
                 alumneNou.Nom+"','"+alumneNou.Llinatge1+"','"+alumneNou.Llinatge2+"')")
connexio.commit()
