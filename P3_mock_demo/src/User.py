from . import Travellers as tv
from Travellers import *
import os
import os.path

class User:

    def __init__(self, Nom, DNI, dir, NT, email):
        self.Nom = Nom
        self.DNI = DNI
        self.dir = dir #dirección postal
        self.NT = NT #num. telefono
        self.email = email

    def get_Nom(self) -> str:
        return self.Nom
    def get_DNI(self) -> int:
        return self.DNI
    def get_dir(self) -> str:
        return self.dir
    def get_NT(self) -> int:
        return self.NT
    def get_email(self) -> str:
        return self.email




