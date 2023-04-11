_A='./BD/tutorialalumnes.db'
import sqlite3
class Alumne:
        nom='';llinatge1='';llinatge2='';edat=0;id=0
        def __init__(A,*B):
                if len(B)==1:C=A.mostrarAlumneBD(B[0]);A.nom=C[3];A.llinatge1=C[1];A.llinatge2=C[2];A.edat=C[4] 
                else:A.defineixNouAlumne(B[0],B[1],B[2],B[3])
        def defineixNouAlumne(A,nom,llinatge1,llinatge2,edat):A.nom=nom;A.llinatge1=llinatge1;A.llinatge2=llinatge2;A.edat=edat
        def guardaraBD(A):C="','";B=sqlite3.connect(_A);D=B.cursor();E=D.execute('INSERT INTO LlistatAlumnes(Edat,Nom,Llinatge1,Llinatge2) values                          ('+str(A.edat)+",'"+A.nom+C+A.llinatge1+C+A.llinatge2+"')");B.commit();B.close();A.id=E.lastrowid;return A.id
        def mostrarAlumneBD(D,id):A=sqlite3.connect(_A);B=A.cursor();C=B.execute('SELECT * from LlistatAlumnes where idAlumne='+str(id)+';');return C.fetchone()
        def eliminarAlumneBD(C):
                A=sqlite3.connect(_A);B=A.cursor();B.execute('DELETE from LlistatAlumnes where idAlumne='+str(C.id)+';');A.commit()
                if B.rowcount==1:return True
                else:return False
        def toString(A):return'Alumne: '+A.nom+' '+A.llinatge1+' '+A.llinatge2+' amb edat '+str(A.edat)+' i id: '+str(A.id)