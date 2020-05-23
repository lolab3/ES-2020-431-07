import os
import os.path
from . import Hotel

class Hotels:

    def __init__(self, h):
        self.Hotels=h
        pass

    def añadirHotel(self, Hotel):
        self.Hotels.append(Hotel)
        self.calculaHotels()

    def eliminarHotel(self, Hotel):
        i=self.Hotels.index(Hotel)
        self.Hotels.pop(i)
        self.calculaHotels()

    def calculaHotels(self):
        preutotal = 0
        for i in self.Hotels:
            preutotal += i.Precio

        return preutotal

    def confirmar_reserva(self, Booking):
        if Booking.confirm_reserve(self.hotels.user, self.hotels):
            print('Reserva del hotel realizada con éxito')
            return True
        else:
            print('Error en la reserva del hotel')
            return False

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