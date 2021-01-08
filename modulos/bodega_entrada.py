import json

class BodegaEntrada():

    def __init__(self):
        self.diccionario = {}
    
    def proveedor(self, nombre_flor, tamaño_flor, cantidad):
        self.nombre_flor = nombre_flor
        self.tamaño_flor = tamaño_flor
        self.cantidad = cantidad
        atributo_flor = {'Nombre': self.nombre_flor, 'Tamaño': self.tamaño_flor, 'Cantidad':self.cantidad}
        self.diccionario[nombre_flor] = atributo_flor
    
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

bodega1 = BodegaEntrada()
bodega1.proveedor('A', 'L', 30)
bodega1.mostrar()
bodega1.proveedor('B', 'S', 10)
bodega1.mostrar()