# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:27:15 2020
@author: Usuario
"""

from P3_mock_demo.src.Destination import Destination
from P3_mock_demo.src.Flights import Flights
from P3_mock_demo.src.Destinations import Destinations
from P3_mock_demo.src.Travel import Travel
from P3_mock_demo.src.Traveller import Traveller
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
hotel2=Hotel('M1291', 'Vela', 2, 1, 7, 500)

listacoches = []
listacoches.append(coche2)
listacoches.append(coche)

C = Car(listacoches)

listahoteles = []
listahoteles.append(hotel)
listahoteles.append(hotel2)

H = Hotels(listahoteles)

Pd.solicitarDatos('MASTERCARD', 'Fernando', 42122343, 872)
viajero = Traveller('Manolo', '12345678P')
V = Travel(f, D, 123, usuari, Pd, C, H, 3, viajero)

#Eliminas destino y vuelo
V.eliminarD('Barcelona')

print('-----------------------------------')
print('testeo clase Viaje añadir:')
V.añadirD('Sevilla', 3)
print('-----------------------------------')
V.añadirV(2134576, 'Sevilla', 23, 3)

print('-----------------------------------')
print('precio total:')

a = V.calcula_preu()
print(a)
print('-----------------------------------')
print('Añadir y eliminar hoteles: ')

for elements in listahoteles:
    print(elements.Nombre)
print('-----------------------------------')
V.eliminarH('Don Candido')
print('-----------------------------------')
V.añadirH('L2310', 'Apolo', 3, 1, 5, 80)
print('-----------------------------------')
print('Añadir y eliminar coches: ')

for elements in listacoches:
    print(elements.Marca)
print('-----------------------------------')
V.eliminarC('Renault')
print('-----------------------------------')
V.añadirC('6677TZ', 'Toyota', 'Badalona', 5, 70)




print('-----------------------------------')
print('Testeo Lista Viajeros')
U = User('Pepito', 1234567, 'Madrid x calle', 633486912, 'grupo@gmail.com')
Tv = Traveller(' ', 0)
d = Destinations(0)
p = PaymentData()
c = Cars('','','','','')
h = Hotels(0)
f = Flights(0)
T = Travel(f, d, 0, U, p, c, h, 1, Tv)
tl = []
tl = T.lista_viajeros(3)
print(tl)
print(tl[0].get_Nom())
print(tl[0].get_DNI())
print(tl[1].get_NomViajero())
print(tl[1].get_DNIViajero())
print(tl[2].get_NomViajero())
print(tl[2].get_DNIViajero())
print(tl[3].get_NomViajero())
print(tl[3].get_DNIViajero())
print(T.NViajeros)