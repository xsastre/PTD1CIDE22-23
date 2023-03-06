class Estudiant:
    school = "freeCodeCamp.org"

    def __init__(self, nom, curs):
        self.nom = nom
        self.curs = curs


Estudiant1 = Estudiant("Jane", "JavaScript")
Estudiant2 = Estudiant("John", "Python")

print(Estudiant1.nom)  # Jane
print(Estudiant2.nom)  # John