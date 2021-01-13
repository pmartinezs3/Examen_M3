
import random
import string
class Proveedor():   
    
    def __init__(self):
        self.flor  = ""
    
    def generar_flor(self):
        #devuelve nombre y tamaño de flor ramdom
        self.flor = random.choice(string.ascii_lowercase) + random.choice(["S","L"])
        return self.flor
      