class Estudiant:
    school = "freeCodeCamp.org"

    def __init__(self, name, course):
        self.nom = name
        self.curs = course


Estudiant1 = Estudiant("Jane", "JavaScript")
Estudiant2 = Estudiant("John", "Python")

print(Estudiant1.nom)  # Jane
print(Estudiant2.nom)  # John