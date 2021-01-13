from modulos import Proveedor, BodegaEntrada, DisenoRamo, FabricaRamo

proveedor = Proveedor()
bodega = BodegaEntrada()
disenoramo = DisenoRamo()
fabrica = FabricaRamo()

# bodega_salida = BodegaSalida()


for i in range(1):
    flor = proveedor.generar_flor()
    bodega.guardar_flor(flor)
    contenido_bodega = bodega.contenido_bodega()
    diseno = disenoramo.disenos()
    ramos_factibles = fabrica.obtener_ramos_factibles(diseno,contenido_bodega)
    # if len(ramos_factibles) == 0:
    #     continue
    # else:
    #     ramo = fabrica.fabrica_ramo(ramos_factibles)
    #     bodega_salida.guardar_ramo(ramo)
