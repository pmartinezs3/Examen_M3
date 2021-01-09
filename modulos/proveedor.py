
import random
import string
class Proveedor():    
    def __init__(self):
        pass       
         
    def generadorflores(self):
        lista_tipos = random.choice(string.ascii_lowercase)        
        for letra in lista_tipos:
            print(str(letra)+random.choice(["S","L"]))

proveedor1 = Proveedor()
proveedor1.generadorflores()
