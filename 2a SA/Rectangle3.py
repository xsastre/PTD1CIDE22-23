class Rectangle():
    base=0
    alsada=0
    area=0 

    def __init__(self,b,a) -> None:
        self.base=b
        self.alsada=a

    def retornaArea(self):
        if self.area==0:
            self.area=self.base * self.alsada
        return self.area
    
    def setBase(self,b):
        self.base=b
    
    def setAlsada(self,a):
        self.alsada=a
    
    def getBase(self):
        return self.base
    
    def getAlsada(self):
        return self.alsada