import json

class BodegaEntrada():

    def __init__(self):
        self.florres = {}        
    
    
    def guardar_flor(self,flor):
         
    
    def mostrar(self):
        print()
        for nombre, valor in self.diccionario.items():
            print("-----")
            nombre = valor["Nombre"]
            tamaño = valor["Tamaño"]
            cantidad = valor["Cantidad"]
            print("Nombre: {} | Tamaño {} | Cantidad {}".format(nombre, tamaño, cantidad))
            #print("Nombre: {} - A: {} | E: {} | Año: {}".format(nombre, autor, editorial, anio))
        
        with open('datos.json', 'w+') as file:
            json.dump(self.diccionario, file)

    def creacion(self):
        datos = {
                'nombre_flor' : self.nombre_flor,
                'tamaño_flor' : self.tamaño_flor,
                'cantidad' : self.cantidad
                }
        with open('datos.json', 'w') as file:
            json.dump(datos, file)
            print(datos)
            
            
bodega1 = BodegaEntrada()
bodega1.proveedor('A', 'L', 30)
bodega1.mostrar()
bodega1.proveedor('B', 'S', 10)
bodega1.mostrar()
