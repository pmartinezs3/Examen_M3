import json
from os import path
from os import stat
from collections import Counter


class BodegaEntrada:
    def __init__(self):
        pass

    def guardar_flor(self, flor):
        # si data.json existe lee y guarda los datos con append
        data = []
        if path.exists("data.json") and stat("data.json").st_size != 0:
            with open("data.json", "r") as file:
                flores = json.load(file)
                for item in flores:
                    data.append(item)
                data.append(flor)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            # si data json no existe crea la estructura del
            # json con los datos de la primera flor
            data = []
            data.append(flor)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

    def contenido_bodega(self):
        with open("data.json") as file:
            flores = json.load(file)
            cantidad = Counter(flores)
            return cantidad
