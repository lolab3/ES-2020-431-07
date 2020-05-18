# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:40:39 2020

@author: Usuario
"""
from . import PaymentData
from . import Flights
from  import Destination

class Travel:
    
    
    def __init__(self,flight,destinos, idViaje):
        self.f = flight
        self.d = destinos
        self.id=idViaje


    def informacion(self):
        for elements in self.f:
            print(elements.Codigo_vuelo)
        for elements in self.d:
            print(elements.destinacion)
    
    def eliminarD(self,dest):
        self.d.eliminarDestino(dest)
        self.f.eliminarVuelo(dest)

    def añadirV(self,codigo, destino, precio, pjs):
        self.f.añadirVuelo(codigo, destino, precio, pjs)
       
    
    def añadirD(self,lugar, dias):
        self.d.añadirDestino(lugar, dias)



    def lista_viajeros(self, num, t: tv): #num de viajeros aparte del user >= 1
        l = []
        l.append(self)

        if num >= 1:
            self.set_NViajeros(num+1) #num de viajeros incluido el user
            for v in range(self.NViajeros-1): #sin contar el user
                l.append(t.Travellers('Viajero', v+1))#su DNI será un número

        return l

    def calcula_preu(self):
        preutotal = 0
        for i in self.precio:
            preutotal += i
        self.precio = preutotal
        return preutotal
