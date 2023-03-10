class Llista:

    def __init__(self):
        self.dades = []
        self.actual = 0
        self.num = 0

    def seleccionar(self, nombre):
        if (nombre>self.num):
            return False
        else:
            self.actual = nombre
            return True

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
        return self.num==0 ## Nova forma d'implementar la funció Equival a if (self.num==0): return TRUE else: return FALSE
    
    def quants(self):
        return self.num


l = Llista()        ## Cream una instància de la classe llista i l'anomenem l

l.afegir("Joana")           ## Afegim l'element "Joana" a la llista l
print (l.seleccionar(10))    ## Seleccionem 1 com la posició actual de la llista
l.afegir("Maria")           ## Afegim un nou element a la posició actual de la llista
print (l.seleccionar(2))    ## Seleccionem 2 com la posició actual de la llista
l.afegir("Moha")            ## Afegim un nou element a la posició actual de la llista
print (l.seleccionar(1))    ## Seleccionem 1 com la posició actual de la llista
l.afegir("Kevin")           ## Afegim un nou element a la posició actual de la llista

## Bucle per mostrar tots els elements de la llista segons la seva posició a la llista
i = 0
while i < l.quants():
    l.seleccionar(i)
    print(l.consultar())
    i = i + 1


