class Alumne:

    def establirCurs(self,cu):
        self.curs=cu
    def establirEtapa(self, et):
        self.etapa=et
    def establirNomComplet(self, nc):
        self.nomcomplet=nc
    def contestarPreguntesProfesor(self,pregunta):
        if (pregunta=="fa bon dia?"):
            return "Sí"
        elif (pregunta=="Com te noms?"):
            return self.nc
        else:
            return "No ho sé"
