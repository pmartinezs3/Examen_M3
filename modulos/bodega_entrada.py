import json
from os import path

class BodegaEntrada():

    def __init__(self,flor):
        self.flor = flor
    
    def guardar_flor(self):
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
            data = []
            Flores = {}
            Flores['nombre'] = self.flor['nombre']
            Flores['tamano'] = self.flor['tamano']
            data.append(Flores)
            with open('data.json','w') as file:
                json.dump(data, file, indent=4)

        
        
          
  
