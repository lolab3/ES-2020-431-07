# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:40:39 2020

@author: Usuario
"""

from P3_mock_demo.src.Flights import Flights

from . import PaymentData as PD
from . import Flights as Fls
from . import Flight as Fl
from . import Destinations as Ds
from . import Cars as Cs
from . import Destination
from . import Bank
from . import User as Us
from . import Skyscanner
from . import Hotel as H
from . import Traveller as Tv
from . import Hotels as Hs
from . import ListCars as C

class Travel:

    def __init__(self, flight: Fls, destinos: Ds, idViaje, usuario : Us, datos_pago: PD, Coches: C, Hoteles: Hs, NViajeros: int, viajero: Tv):
        self.f = flight
        self.d = destinos
        self.id = idViaje
        self.data_payment = datos_pago
        self.user = usuario
        self.coches=Coches
        self.hoteles=Hoteles
        self.NViajeros = 1 #el user siempre
        self.viajeros = viajero

    def set_NViajeros(self, num):

        self.NViajeros = num
    def get_NViajeros(self):
        return self.NViajeros

    def informacion(self):
        for elements in self.f:
            print(elements.Codigo_vuelo)
        for elements in self.d:
            print(elements.destinacion)

    def eliminarD(self, dest):
        self.d.eliminarDestino(dest)
        self.f.eliminarVuelo(dest)


    def añadirV(self, codigo, destino, precio, pjs):
        self.f.añadirVuelo(codigo, destino, precio, pjs)


    def añadirD(self, lugar, dias):
        self.d.añadirDestino(lugar, dias)


    def añadirH(self, codigo, nom, nHostes, nHabitacions, durada, preu):
        self.hoteles.añadirHotel(codigo, nom, nHostes, nHabitacions, durada, preu)


    def eliminarH(self, nom):
        self.hoteles.eliminarHotel(nom)


    def añadirC(self, codigo, marca, sitio_recogida, dias, precio):
        self.coches.añadirCar(codigo, marca, sitio_recogida, dias, precio)


    def eliminarC(self, marca):
        self.coches.eliminarCar(marca)




    def lista_viajeros(self, num): #num de viajeros aparte del user >= 1
        l = []
        l.append(self.user)#guarda un objeto user con todos sus datos
        if num >= 1:
            self.set_NViajeros(num+1) #num de viajeros incluido el user
            for i in range(0, num):
                t = Tv.Traveller('Viajero', i)
                l.append(t)

        self.viajeros = l
        return l

    def calcula_preu(self):
        preciovuelos = self.f.calculaflights()
        preciocoches= self.coches.calculaCars()
        precioHoteles=self.hoteles.calculaHotels()
        preciototal=preciocoches+precioHoteles+preciovuelos
        return preciototal

    def Pago_viaje(self, Bank):
        tarjetas = ['MASTERCARD', 'VISA']
        if self.data_payment.getCardType() in tarjetas:
            if Bank.do_payment(self.user, self.data_payment):
                print('pago realizado correctamente')
                return True
            else:
                print('error en la entidad bancaria')
                return False
        else:
            print('error en el tipo de tarjeta')
            return False


    def confirmar_reserva_vuelos(self, Skyscanner):
        if Skyscanner.confirm_reserve(self.user, self.f):
            print('reserva de vuelos realizada con exito')
            return True
        else:
            print('error en la reserva de vuelos')
            return False

    def confirmar_reserva_vehículos(self, Rentalcars):
        if Rentalcars.confirm_reserve(self.user, self.coches):
            print('Reserva del coche realizada con éxito')
            return True
        else:
            print('Error en la reserva del coche')
            return False

    def confirmar_reserva_hoteles(self, Booking):
        if Booking.confirm_reserve(self.user, self.Hoteles):
            print('Reserva del hotel realizada con éxito')
            return True
        else:
            print('Error en la reserva del hotel')
            return False

    def confirmar_reserva(self, Skyscanner, Rentalcars, Booking):
        b = False
        if self.confirmar_reserva_vuelos(Skyscanner):
            if self.confirmar_reserva_vehículos(Rentalcars):
                if self.confirmar_reserva_hoteles(Booking):
                    b = True

        return b