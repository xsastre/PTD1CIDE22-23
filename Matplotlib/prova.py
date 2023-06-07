#els tres nombres de la equació
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
float(discriminante);
float(resultado_raiz);
#resolem el discriminant
#elevam a 0.5 (és el mateix que fer la arrel quadrada)
discriminante = b**(2)-4*a*c
resultado_raiz = discriminante**(0.5)
#en cas de que l'arrel sigui positiva continuam
if discriminante > 0:
    eq1 = (-b+resultado_raiz)/(2*a)
    eq2 = (-b-resultado_raiz)/(2*a)
    print("sol 1:" + str(eq1))
    print("sol 2: " + str(eq2))
else:
    print("arrel negativa, NTSR")

