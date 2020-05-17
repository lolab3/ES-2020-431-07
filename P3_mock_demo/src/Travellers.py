class Travellers:

    def __init__(self, Nombre, DNI):
        self.Nombre = Nombre
        self.DNI = DNI
    def get_NomViajero(self) -> str:
        return self.Nombre
    def get_DNIViajero(self) -> int:
        return self.DNI