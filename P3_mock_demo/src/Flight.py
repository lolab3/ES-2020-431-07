class Flight(object):

    def __init__(self, codigo, destino, precio, pjs):
        self.Codigo_vuelo = codigo
        self.Destinacion = destino
        self.precio = precio
        self.N_pjs = pjs

    def informacion(self):
        print(self.Codigo_vuelo)
        print(self.Destinacion)
        print(self.precio)
        print(self.N_pjs)

         
    
        
