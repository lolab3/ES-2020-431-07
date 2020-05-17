from . import Travellers as tv
from Travellers import *

class User:

    def __init__(self, Nom: str, DNI:int , dir: str, NT: int, email: str):
        self.Nom = Nom
        self.DNI = DNI
        self.dir = dir #dirección postal
        self.NT = NT #num. telefono
        self.email = email
        self.reserves #lista de reservas donde estarán todos los vuelos/coches/hoteles que ha adquirido este usuario

    def get_Nom(self) -> str:
        return self.Nom
    def get_DNI(self) -> int:
        return self.DNI
    def get_Dir(self) -> str:
        return self.dir
    def get_NT(self) -> int:
        return self.NT
    def get_email(self) -> str:
        return self.email





