from P3_mock_demo.src.Cars import Cars

class Car:

    def __init__(self, Cars):
        self.cars = Cars

    def añadirCar(self, codigo, marca, sitio_recogida, dias, precio):
        v = Cars(codigo, marca, sitio_recogida, dias, precio)
        self.cars.append(v)
        for elements in self.cars:
            print(elements.Marca)

    def eliminarCar(self, marca):
        i = 0
        for elements in self.cars:
            if elements.Marca == marca:
                borrar = i
            else:
                i = i + 1
        self.cars.pop(borrar)
        for elements in self.cars:
            print(elements.Marca)

    def calculaCars(self):
        preutotal = 0
        for i in self.cars:
            preutotal += i.Precio * i.Dias
        return preutotal

