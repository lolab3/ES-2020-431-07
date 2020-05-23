# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:40:39 2020

@author: Usuario
"""

from P3_mock_demo.src.Flights import Flights

from . import PaymentData
from . import Flights
from . import Flight
from . import Destinations
from . import Destination
from . import Bank
from . import User
from . import Skyscanner


class Travel:

    def __init__(self, flight, destinos, idViaje, usuario, datos_pago, Coches, Hoteles):
        self.f = flight
        self.d = destinos
        self.id = idViaje
        self.data_payment = datos_pago
        self.user = usuario
        self.coches=Coches
        self.hoteles=Hoteles

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
        self.calcula_preu()

    def añadirD(self, lugar, dias):
        self.d.añadirDestino(lugar, dias)

    # def lista_viajeros(self, num, t: tv): #num de viajeros aparte del user >= 1
    # l = []
    # l.append(self)

    # if num >= 1:
    # self.set_NViajeros(num+1) #num de viajeros incluido el user
    # for v in range(self.NViajeros-1): #sin contar el user
    # l.append(t.Travellers('Viajero', v+1))#su DNI será un número

    # return l

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

    def confirmar_reserva(self, Skyscanner):
        if Skyscanner.confirm_reserve(self.user, self.f):
            print('reserva realizada con exito')
            return True
        else:
            print('error en la reserva')
            return False