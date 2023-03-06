class Llista:
    dades = []
    actual = 0
    num = 0
    def __int__(self):
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

class Pila:
    dades=[]
    def __int__(self):
        self.dades=[]
    def apilar(self,element):
        self.dades.append(element)
    def desapilar(self):
        self.dades.pop(0)                   ## Eliminarem el primer element de la pila (funcionament FIFO - first in, first out)
        #self.dades.pop(len(self.dades)-1)   ## Eliminarem el darrer element de la pila (exemple pila de plats quan els posem a una pica
    def buida(self):
        return len(self.dades)==0
    def llistaElements(self):
        llistaAux=[]
        for index in range(len(self.dades)):
            llistaAux.insert(index,self.dades[index])
        return llistaAux

p = Pila()        ## Cream una instància de la classe llista i l'anomenem l

p.apilar("Joana")           ## Afegim l'element "Joana" a la pila l
p.apilar("Maria")           ## Afegim un nou element a la pila l
p.apilar("Moha")            ## Afegim un nou element a la posició actual de la llista
p.apilar("Kevin")           ## Afegim un nou element a la posició actual de la llista
print(str(p.llistaElements()))
p.desapilar()
print("Es buida la pila? ",p.buida())
print(str(p.llistaElements()))



