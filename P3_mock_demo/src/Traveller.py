class Traveller:

    def __init__(self, Nombre:str, DNI:int):
        self.Nombre = Nombre
        self.DNI = DNI
    def set_Nom(self, nom):
        self.Nombre = nom
    def set_DNI(self, dni):
        self.DNI = dni
    def get_NomViajero(self):
        return self.Nombre
    def get_DNIViajero(self):
        return self.DNI