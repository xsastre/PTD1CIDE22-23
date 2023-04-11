from AlumneBDminified import *
nouAlumne=Alumne('Llorenç','Capellà','Vich',34)
print(nouAlumne.toString()+" creat satisfactòriament.")
idnouAlumne=nouAlumne.guardaraBD()
print(nouAlumne.toString()+" guardat a la BD correctament.")
print(nouAlumne.mostrarAlumneBD(idnouAlumne))
if (nouAlumne.eliminarAlumneBD()):
    print(nouAlumne.toString()+" eliminat de la BD correctament")
else:
    print(nouAlumne.toString()+" no s'ha eliminat de la BD")
anticAlumne=Alumne(2)
print(anticAlumne.nom)
