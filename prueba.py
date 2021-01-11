
import json


with open('data.json') as file:
    flores = json.load(file)
    nueva_lista = []
    item_encontrados = []
    for flor in flores:
        if (not flor in item_encontrados):
            item_encontrados.append(flor)
            contar = flores.count(flor)
            if contar > 0:
                nuevo_elemento = {}
                nuevo_elemento['nombre'] = flor['nombre']
                nuevo_elemento['tamano'] = flor['tamano']
                nuevo_elemento['cantidad'] = contar
                nueva_lista.append(nuevo_elemento)
    print(nueva_lista)