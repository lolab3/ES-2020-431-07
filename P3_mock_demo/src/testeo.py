# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:27:15 2020

@author: Usuario
"""

from P3_mock_demo.src.Destination import Destination
from P3_mock_demo.src.Flights import Flights
from P3_mock_demo.src.Destinations import Destinations
from P3_mock_demo.src.Travel import Travel
from P3_mock_demo.src.Flight import Flight
from P3_mock_demo.src.Cars import Cars
from P3_mock_demo.src.ListCars import Car
from P3_mock_demo.src.Hotel import Hotel
from P3_mock_demo.src.Hotels import Hotels
from P3_mock_demo.src.User import User
from P3_mock_demo.src.PaymentData import PaymentData





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
D.info()
print('-----------------------------------')
#testeo clase Viaje
print('testeo clase Viaje eliminar:')
usuari=User('Fernando', '0000000A', 'Carrer Montblanc', '103860647', 'fernando@ejemplo.com')
Pd = PaymentData()
coche=Cars('6677TZ', 'Renault', 'Terrassa', 10, 100)
coche2=Cars('1238TL', 'Opel', 'Barcelona', 5, 60)
hotel=Hotel('L2310', 'Don Candido', 3, 1, 5, 120)
hotel2=Hotel('M1291', 'Vela', 2, 1, 7, 2000)

listacoches=Car([])
listacoches.añadirCoche(coche2)
listacoches.añadirCoche(coche)

listahoteles=Hotels([])
listahoteles.añadirHotel(hotel)
listahoteles.añadirHotel(hotel2)

Pd.solicitarDatos('MASTERCARD', 'Fernando', 42122343, 872)

V = Travel(f, D, 123, usuari, Pd, listacoches, listahoteles)
#Eliminas destino y vuelo
V.eliminarD('Barcelona')
print('-----------------------------------')
print('testeo clase Viaje añadir:')
V.añadirD('Sevilla', 3)
print('-----------------------------------')
V.añadirV(2134576, 'Sevilla', 23, 3)



print('-----------------------------------')
print('precio total:')
total = V.calcula_preu()
print(total)


print('Añadir y eliminar coches: ')



for i in listacoches.cars:
    print(i.Codigo_coche)
    print(i.Marca)

listacoches.eliminarCoche(coche)
print('-----------------------------------')
for i in listacoches.cars:
    print(i.Codigo_coche)
    print(i.Marca)

print('Añadir y eliminar hotles: ')



for i in listahoteles.Hotels:
    print(i.Nombre)

listahoteles.eliminarHotel(hotel)
print('-----------------------------------')
for i in listahoteles.Hotels:
    print(i.Nombre)

