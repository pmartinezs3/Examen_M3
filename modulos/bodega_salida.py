
from bodega_entrada import *

class BodegaSalida(BodegaEntrada):

    def __init__(self,ramo):
        self.ramos = list()
        

    def lista_ramos_fabricados(self,ramo):
        self.ramos.append(ramo)
    
    
        
