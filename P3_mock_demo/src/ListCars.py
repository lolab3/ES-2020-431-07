from . import Cars
from . import Rentalcars

class Car:

    def __init__(self, cars, user):
        self.cars = cars

    def añadirCoche(self, car):
        self.cars.append(car)
        self.calculaCars()

    def eliminarCoche(self, car):
        i=self.cars.index(car)
        self.cars.pop(i)
        self.calculaCars()

    def calculaCars(self):
        preutotal = 0
        for i in self.cars:
            preutotal += i.Precio
        return preutotal

    def confirmar_reserva(self, Rentalcars):
        if Rentalcars.confirm_reserve(self.cars.user, self.cars):
            print('Reserva del coche realizada con éxito')
            return True
        else:
            print('Error en la reserva del coche')
            return False