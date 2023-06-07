import matplotlib.pyplot as plt
import numpy as np

def dibujar_parabola(a, b, c):
    x = np.linspace(-10, 10, 4)  # Generar 400 puntos en el rango de -10 a 10
    y = a * x**2 + b * x + c  # Calcular los valores de y para cada x

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de la ecuación cuadrática: y = {}x^2 + {}x + {}'.format(a, b, c))
    plt.grid(True)
    plt.show()

# Solicitar los valores de a, b y c
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Dibujar la parábola
dibujar_parabola(a, b, c)
