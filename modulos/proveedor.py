
import random
import string
class Proveedor():   
    
    def __init__(self):
        self.flor  = ""
        self.tamano = ""
    
    def generar_flor(self):
        #devuelve nombre y tamaño de flor ramdom
        self.flor = random.choice(string.ascii_lowercase)
        self.tamano = random.choice(["S","L"])
        return {"nombre":self.flor ,"tamano":self.tamano}
      