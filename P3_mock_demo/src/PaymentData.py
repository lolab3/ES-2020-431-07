import Viaje as V
class PaymentData:
    def __init__(self, V):
        # V2 self.Tipus_targeta = ''
        self.Nom = ''
        self.Numero_targeta = 0
        self.CodiSeguretat = 0
        self.Import = calculaprecio(V)

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


