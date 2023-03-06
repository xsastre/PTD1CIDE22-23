class Llista:
    dades = []
    actual = 0
    num = 0
    def __int__(self):
        self.dades = []
        self.actual = 0
        self.num = 0

    def seleccionar(self, nombre):
        self.actual = nombre

    def afegir(self, element):
        self.dades.insert(self.actual, element)
        self.num = self.num + 1

    def extreure(self):
        self.num = self.num - 1
        return self.dades.pop(self.actual)

    def consultar(self):
        return self.dades[self.actual]

    def buida(self):
        # return len(self.dades) == 0
        return self.num==0

    def quants(self):
        return self.num



