
import random
import string
class Proveedor():    
    def __init__(self):
        self.flor  = ""
         
    def generadorflores(self):
        self.flor = random.choice(string.ascii_lowercase) + random.choice(["S","L"])
        return self.flor 
      