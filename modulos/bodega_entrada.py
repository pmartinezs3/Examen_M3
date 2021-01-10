import json
from os import path

class BodegaEntrada():

    def __init__(self,flor):
        self.flor = flor #resive flor = nombre y tamaño en un objeto
    
    def guardar_flor(self):
        # si data.json existe lee y guarda los datos con append
        data = []
        if path.exists('data.json'):
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

        
        
          
  
