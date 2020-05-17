# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:46:48 2020

@author: Usuario
"""
import Destination

class Destinations:
    
    def __init__(self,destination):
        self.dest = destination
        
    def info(self):
        for elements in self.dest:
            print(elements.destinacion)
            
    def eliminarDestino(self,destino):
        i = 0
        for elements in self.dest:
            if elements.destinacion == destino:
                borrar = i
            else:
                i = i+1
        
        
        self.dest.pop(borrar)        
        for elements in self.dest:
            print(elements.destinacion)
            
    def añadirDestino(self, lugar, dias):
        d = Destino(lugar, dias)
        self.dest.append(d)
        for elements in self.dest:
            print(elements.destinacion)
    
    
    