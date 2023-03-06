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

rectangle = Rectangle(20, 10)
triangle = Triangle(20, 12)

print("Àrea del rectangle: ", rectangle.area())
print("Área del triangle:", triangle.area())