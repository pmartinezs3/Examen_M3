
from modulos import Proveedor, BodegaEntrada,FabricaRamo

proveedor = Proveedor()
bodega = BodegaEntrada()
fabrica = FabricaRamo()
bodega_salida = BodegaSalida()
disenos = Disenos()

while True:
    flor = proveedor.generar_flor()
    bodega.guardar_flor(flor)
    contenido_bodega = bodega.contenido_bodega()
    ramos_factibles = fabrica.obtener_ramos_factibles(disenos,contenido_bodega)
    if len(ramos_factibles) == 0:
        continue
    else:
        ramo = fabrica.fabrica_ramo(ramos_factibles)
        bodega_salida.guardar_ramo(ramo)
        
        
    
    