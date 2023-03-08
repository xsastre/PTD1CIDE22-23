from typing import Any


class Cotxe:
    rodes= 4

    def __init__(self,color, acceleracio):
        self.color = color
        self.acceleracio = acceleracio
        self.velocitatActual = 50

    def accelera(self):
        self.velocitatActual = self.velocitatActual+self.acceleracio

    def frena(self):
        velocitat = self.velocitatActual -self.acceleracio
        if velocitat < 0:
            velocitat=0
        self.velocitatActual=velocitat

    def mostraPropietats(self):
        text = str(self.velocitatActual) + " " + str(self.color) + " " + str(self.rodes) + " " + str(self.acceleracio)
        return text

c1 = Cotxe("vermell",20)
c2 = Cotxe("blau",30)
twingo = Cotxe("blau",40)
bmw = Cotxe("verd",150)
#print(twingo.acceleracio)
print(bmw.mostraPropietats())
print(twingo.mostraPropietats())
bmw.frena()
print(bmw.mostraPropietats())