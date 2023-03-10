class Rectangle:
    
    def __init__(self,b,a) -> None:
        self.base=b
        self.alsada=a

    def retornaArea(self):
        return self.base * self.alsada
    
    def setBase(self,b):
        self.base=b
    
    def setAlsada(self,a):
        self.alsada=a
    
    def getBase(self):
        return self.base
    
    def getAlsada(self):
        return self.alsada