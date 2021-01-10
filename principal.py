
from modulos import *

proveedor1 = Proveedor()
bodega = BodegaEntrada(proveedor1.generadorflores())
bodega.guardar_flor()
bodega.contar_flores()




