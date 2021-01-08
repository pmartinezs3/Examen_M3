import json

class BodegaEntrada():

    def __init__(self, nombre_flor, tamaño_flor, cantidad):
        self.nombre_flor = nombre_flor
        self.tamaño_flor = tamaño_flor
        self.cantidad = cantidad  

    def creacion(self):
        datos = {
                'nombre_flor' : self.nombre_flor,
                'tamaño_flor' : self.tamaño_flor,
                'cantidad' : self.cantidad
                }
        with open('datos.json', 'w') as file:
            json.dump(datos, file)
            print(datos)
            
            
