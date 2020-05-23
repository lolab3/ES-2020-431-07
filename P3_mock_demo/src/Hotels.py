import os
import os.path
from P3_mock_demo.src.Hotel import Hotel

class Hotels:

    def __init__(self, h):
        self.Hotels=h
        pass

    def añadirHotel(self, codigo, nom, nHostes, nHabitacions, durada, preu):
        v = Hotel(codigo, nom, nHostes, nHabitacions, durada, preu)
        self.Hotels.append(v)
        for elements in self.Hotels:
            print(elements.Nombre)

    def eliminarHotel(self, nom):
        i = 0
        for elements in self.Hotels:
            if elements.Nombre == nom:
                borrar = i
            else:
                i = i + 1
        self.Hotels.pop(borrar)
        for elements in self.Hotels:
            print(elements.Nombre)

    def calculaHotels(self):
        preutotal = 0
        for i in self.Hotels:
            preutotal += i.Precio * i.numHabitaciones * i.duracion

        return preutotal



    def rm(self, filename):
        """Dummy function to remove a file.

        Args:
            filename (str): path to the file.
        """    
        if os.path.isfile(filename):
            os.remove(filename)
    
    @staticmethod
    def get_always_true():
        """Dummy function to return always true

        Returns:
            [bool]: Return true.
        """        
        return True