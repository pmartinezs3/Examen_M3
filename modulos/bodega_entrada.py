import json
from os import path 
from os import stat

class BodegaEntrada():

    def __init__(self):
        pass
    
    def guardar_flor(self,flor):
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
        with open('data.json') as file:
            flores = json.load(file)
            item_encontrados = []
            for flor in flores:
                self.lista_flores.append(flor)
                
            print(self.lista_flores)
        #         if (not flor in item_encontrados):
        #             item_encontrados.append(flor)
        #             contar = flores.count(flor)
        #             if contar > 0:
        #                 nuevo_elemento = {}
        #                 nuevo_elemento['nombre'] = flor['nombre']
        #                 nuevo_elemento['tamano'] = flor['tamano']
        #                 nuevo_elemento['cantidad'] = contar
        #                 self.cantidad_flores.append(nuevo_elemento)
        
        # for cantidad in self.cantidad_flores:
        #     print(cantidad)
    