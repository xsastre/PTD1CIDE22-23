from AlumneBDminified import *
nouAlumne=Alumne('Llorenç','Capellà','Vich',34)
print(nouAlumne.toString()+" creat satisfactòriament.")
idnouAlumne=nouAlumne.guardaraBD()
nouAlumne2=Alumne('Tofol','Verdera','Damià',23)
idnouAlumne2=nouAlumne2.guardaraBD()
print(nouAlumne.toString()+" guardat a la BD correctament.")
print(nouAlumne.mostrarAlumneBD(idnouAlumne))
print(nouAlumne2.mostrarAlumneBD(idnouAlumne2))
if (nouAlumne.eliminarAlumneBD()):
    print(nouAlumne.toString()+" eliminat de la BD correctament")
else:
    print(nouAlumne.toString()+" no s'ha eliminat de la BD")
anticAlumne=Alumne(2)
print(nouAlumne.nom)
print(nouAlumne.mostrarAlumneBD(22))
print(anticAlumne.nom)
