# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:40:39 2020

@author: Usuario
"""

from Flights import Flights
from Destinos import Destinos

class Viaje:
    
    
    def __init__(self,flight,destinos):
        self.f = flight
        self.d = destinos
    
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
        