
import random
import string
class Proveedor():    
    def __init__(self):
        self.flor  = ""
        self.tamano = ""
    
    def generadorflores(self):
        self.flor = random.choice(string.ascii_lowercase)
        self.tamano = random.choice(["S","L"])
        return {"nombre":self.flor ,"tamano":self.tamano}
      