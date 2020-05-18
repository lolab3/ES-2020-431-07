# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:27:15 2020

@author: Usuario
"""

from vols import Vuelos
from Destino import Destino
from Flights import Flights
from Destinos import Destinos
from Viaje import Viaje

#testeo clase Vuelo y Flights
print('testeo clase Vuelo y Flights:')
v1 = Vuelos(1234567, 'Barcelona', 35, 4)
v2 = Vuelos(3215674, 'Madrid', 40, 3)

v = []
v.append(v1)
v.append(v2)

f = Flights(v)
f.informacion()
print('-----------------------------------')
#testeo clase Destino y Destinos
print('testeo clase Destino y Destinos:')
d1 = Destino('Barcelona', 5)
d2 = Destino('Madrid', 4)

r = []
r.append(d1)
r.append(d2)

D = Destinos(r)
D.informacion()
print('-----------------------------------')
#testeo clase Viaje
print('testeo clase Viaje eliminar:')
V = Viaje(f,D)
V.eliminarD('Barcelona')
print('-----------------------------------')
print('testeo clase Viaje añadir:')
V.añadirD('Sevilla', 3)
print('-----------------------------------')
V.añadirV(2134576,'Sevilla', 23, 3)


print('precio total:')
print('-----------------------------------')
total = f.calcula_preu()
print(total)