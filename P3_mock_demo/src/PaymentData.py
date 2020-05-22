from . import Travel


class PaymentData:
    def __init__(self, v:Travel):
        self.Tipus_targeta = ''
        self.Nom = ''
        self.Numero_targeta = 0
        self.CodiSeguretat = 0
        self.Import = v.calcula_preu()

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

    def confirmarPago(self, valido):
        if (valido == True):
            print ('Pago realizado correctamente con', self.Tipus_targeta)
        else:
            print('Error en el pago, vuelva a intentarlo')
