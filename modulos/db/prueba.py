import json
from os import path

def guardardatos():
    data = []
    if path.exists('data.json'):
        with open('data.json','r') as file:
            flores = json.load(file)
            for flor in flores:
                data.append(flor)
        data.append({'nombre':"g",'tamano':'L','cantidad': 100})
        print(data)
        with open('data.json','w') as file:
            json.dump(data,file, indent=4)
    else:
        data = []
        Flores = {}
        Flores['nombre'] = 'r'
        Flores['tamano'] = 'S'
        Flores['cantidad'] = 50
        data.append(Flores)
        with open('data.json','w') as file:
            json.dump(data, file, indent=4)
            
              
guardardatos()
  
        
