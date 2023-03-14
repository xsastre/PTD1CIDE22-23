from accessorisCotxe import any

class Cotxe:

    ## Definició d'atributs
    tipusdeCanvi = TipusdeCanvi.MANUAL ## Definir com a tipus ("Manual","Automàtic")
    marxaActual = Marxa.PuntMort ## Definir marxes com tipus 
    revolucions = 0
    revolucionsMaximes = 10000
    tipusCarburant = Carburant.BENZINA ## Definir com a tipus ("Benzina","Dièsel","Híbrid","Elèctric")
    ## Definir mètode càlcul d'autonomia en kms en funcio del tipus de Carburant
    embraguePitjat = False
    motorGripat = False
    estatMotor = 0 ## Definir com a tipus ("Encès", "Apagat")
    acceleracioActual = 0

    ## sets i gets

    def encendreMotor(self):
        pass

    def aturarMotor(self):
        pass

    def canvideMarxa(self,marxa):
        pass

    def pitjarAccelerador(self,acceleracio):
        pass

    def pitjarFre(self,desacceleracio):
        pass

    def griparMotor(self):
        pass


