from . import Travel
class PaymentData:
    def __init__(self, Travel):
        # V2 self.Tipus_targeta = ''
        self.Nom = ''
        self.Numero_targeta = 0
        self.CodiSeguretat = 0
        self.Import = calcula_preu(Travel)

    def solicitarDatos(self, tipus, nom, numero, codi):
        # V2 self.Tipus_targeta = tipus
        self.Nom = nom
        self.Numero_targeta = numero
        self.CodiSeguretat = codi

    def validarDatosPago(self):

        if (type(self.Tipus_targeta, self.nom) != str or type(self.Numero_targeta, self.CodiSeguretat) != int or type(
                self.Import) != float):
            return False
        else:
            return True


