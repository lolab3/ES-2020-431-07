

class PaymentData:
    def __init__(self):
        self.Tipus_targeta = ''
        self.Nom = ''
        self.Numero_targeta = 0
        self.CodiSeguretat = 0
        self.Import = 0

    def solicitarDatos(self,tipus,nom,numero,codi):
        self.Tipus_targeta = tipus
        self.Nom = nom
        self.Numero_targeta = numero
        self.CodiSeguretat = codi

    def validarDatosPago(self):
        if((type(self.Tipus_targeta) and type(self.Nom) != str) or (type(self.Numero_targeta) and type(self.CodiSeguretat) and type(self.Import) != int )):
            return False
        else:
            return True


    def getCardType(self):
        return self.Tipus_targeta

