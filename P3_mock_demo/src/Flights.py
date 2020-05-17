from Flight import Flight

class Flights:

    def __init__(self,Flight):
        self.flights = Flight
            
    def informacion(self):
        for elements in self.flights:
            print(elements.Destinacion)

    def añadirVuelo(self,codigo, destino, precio, pjs):
        v = Flight(codigo, destino, precio, pjs)
        self.flights.append(v)
        for elements in self.flights:
            print(elements.Codigo_vuelo)
            
    def eliminarVuelo(self,dest):
        i = 0
        for elements in self.flights:
            if elements.Destinacion == dest:
                borrar = i 
            else:
                i = i+1
        
        
        self.flights.pop(borrar)
        for elements in self.flights:
            print(elements.Destinacion)
    