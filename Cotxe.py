class Cotxe():
    rodes = 4

    def __init__(self,color, acceleracio):
        self.color = color
        self.acceleracio = acceleracio
        self.velocitatActual = 0

    def accelera(self):
        self.velocitatActual = self.velocitatActual+self.acceleracio

    def frena(self):
        velocitat = self.velocitatActual -self.acceleracio
        if velocitat < 0:
            velocitat=0
        self.velocitatActual=0

c1 = Cotxe("vermell",20)
print(c1.color)