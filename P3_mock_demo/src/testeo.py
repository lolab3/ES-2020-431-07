# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:27:15 2020

@author: Usuario
"""

from . import Destination
from . import Flights
from . import Destinations
from . import Travel
from . import Flight



if __name__ == '__main__':

    #testeo clase Vuelo y Flights
    print('testeo clase Vuelo y Flights:')
    v1 = Flight(1234567, 'Barcelona', 35, 4)
    v2 = Flight(3215674, 'Madrid', 40, 3)

    v = []
    v.append(v1)
    v.append(v2)
    #Lista de vuelos
    f = Flights(v)
    f.informacion()
    print('-----------------------------------')
    #testeo clase Destino y Destinos
    print('testeo clase Destino y Destinos:')
    d1 = Destination('Barcelona', 5)
    d2 = Destination('Madrid', 4)

    #Lista de destinos
    r = []
    r.append(d1)
    r.append(d2)

    D = Destinations(r)
    D.informacion()
    print('-----------------------------------')
    #testeo clase Viaje
    print('testeo clase Viaje eliminar:')
    V = Travel(f, D, 123)
    #Eliminas destino y vuelo
    V.eliminarD('Barcelona')
    print('-----------------------------------')
    print('testeo clase Viaje añadir:')
    V.añadirD('Sevilla', 3)
    print('-----------------------------------')
    V.añadirV(2134576,'Sevilla', 23, 3)


    print('precio total:')
    print('-----------------------------------')
    total = V.calcula_preu()
    print(total)