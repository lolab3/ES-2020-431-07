from . import Travellers as tv
from Travellers import *

class User:

    def __init__(self, Nom, DNI, dir, NT, email, NViajeros=1):
        self.Nom = Nom
        self.DNI = DNI
        self.dir = dir #dirección postal
        self.NT = NT #num. telefono
        self.email = email
        self. NViajeros = NViajeros

    def set_NViajeros(self, num):
        self.NViajeros = num

    def lista_viajeros(self, num, t: tv): #num de viajeros aparte del user >= 1
        l = []
        l.append(self)

        if num >= 1:
            self.set_NViajeros(num+1) #num de viajeros incluido el user
            for v in range(self.NViajeros-1): #sin contar el user
                l.append(t.Travellers('Viajero', v+1))#su DNI será un número

        return l




