# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:46:48 2020

@author: Usuario
"""
from P3_mock_demo.src.Destination import Destination

class Destinations:
    
    def __init__(self, destination):
        self.dest = destination
        
    def info(self):
        for elements in self.dest:
            print(elements.Destination)
            
    def eliminarDestino(self,destino):
        i = 0
        for elements in self.dest:
            if elements.Destination == destino:
                borrar = i
            else:
                i = i+1
        
        
        self.dest.pop(borrar)        
        for elements in self.dest:
            print(elements.Destination)
            
    def añadirDestino(self, lugar, dias):
        des = Destination(lugar, dias)
        self.dest.append(des)
        for elements in self.dest:
            print(elements.Destination)
    
    
    