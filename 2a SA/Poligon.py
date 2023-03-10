class Poligon:
    """
    Defineix un polígon segons la seva base i la seva alçada.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

class Rectangle(Poligon):

    def area(self):
        return self.b * self.h

class Triangle(Poligon):

    def area(self):
        return (self.b * self.h) / 2

