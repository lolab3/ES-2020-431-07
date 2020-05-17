from vols import Vuelos

class Flights:

    def __init__(self,Vuelo):
        self.vuelos = Vuelo
            
    def informacion(self):
        for elements in self.vuelos:
            print(elements.Destinacion)

    def añadirVuelo(self,codigo, destino, precio, pjs):
        v = Vuelos(codigo, destino, precio, pjs)
        self.vuelos.append(v)
        for elements in self.vuelos:
            print(elements.Codigo_vuelo)
            
    def eliminarVuelo(self,dest):
        i = 0
        for elements in self.vuelos:
            if elements.Destinacion == dest:
                borrar = i 
            else:
                i = i+1
        
        
        self.vuelos.pop(borrar)        
        for elements in self.vuelos:
            print(elements.Destinacion)
    