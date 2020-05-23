from . import Cars

class Car:

    def __init__(self, cars):
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