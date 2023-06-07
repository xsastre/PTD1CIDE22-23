class Alumne:
    def __init__(self, nom, curs):
        self.nom = nom
        self.curs = curs
        self.notes=()

alumnes=[]
alumnes.insert(0,Alumne("Tomeu","1r BAT"))
alumnes.insert(1,Alumne("Tofol","1r BAT"))
alumnes[0].notes=(3.5,6,7,8,2.5)
alumnes[1].notes=(3.5,6,7,8,2.5)

print(alumnes[0].notes[1])

numeroalumnes=len(alumnes)
numeronotes=5
comptador=0

mitjana=0
while (comptador < numeroalumnes):
    comptador2=0
    while (comptador2 < numeronotes):
        mitjana+=alumnes[comptador].notes[comptador2]
        comptador+=1
    print("Mitjana ",alumnes[comptador].nom," ",(mitjana/numeronotes))
    comptador+=1