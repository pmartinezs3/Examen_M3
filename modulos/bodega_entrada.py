import json
from os import path 
from os import stat


class BodegaEntrada():

    def __init__(self,flor):
        #resive flor = nombre y tamaño en un objeto
        self.flor = flor 
        #lista de objetos con nombre , tamaño y cantidad de flores en bodega
        self.cantidad_flores = [] 
    
    def guardar_flor(self):
        # si data.json existe lee y guarda los datos con append
        data = []
        if path.exists('data.json') and stat("data.json").st_size != 0:
            with open('data.json','r') as file:
                flores = json.load(file)
                for flor in flores:
                    data.append(flor)
            data.append({"nombre":self.flor['nombre'],"tamano":self.flor['tamano']})
            with open('data.json','w') as file:
                json.dump(data,file,indent=4)
        else:
            # si data json no existe crea la estructura del 
            # json con los datos de la primera flor
            data = []
            Flores = {}
            Flores['nombre'] = self.flor['nombre']
            Flores['tamano'] = self.flor['tamano']
            data.append(Flores)
            with open('data.json','w') as file:
                json.dump(data, file, indent=4)
                
    
    def contar_flores(self):
        item_encontrado = []
        with open('data.json') as file:
            flores = json.load(file)
            for flor in flores:
                if (not flor in item_encontrado):
                    # items_found acumula los dic que ya se analizaron para no repetirlos
                    item_encontrado.append(flor)
                    cuenta_item = flores.count(flor)
                if cuenta_item > 0:
                    item_nuevo = {}
                    item_nuevo['nombre'] = flor['nombre']
                    item_nuevo['tamano'] = flor['tamano']
                    item_nuevo['cantidad'] = cuenta_item
                    self.cantidad_flores.append(item_nuevo)
        print(self.cantidad_flores)
                    
    