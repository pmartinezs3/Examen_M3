
class Flor:
    def __init__(self,especie_flor,tamano_flor):
        self.tamano_flor = tamano_flor
        self.especie_flor = especie_flor
        
        
    def flor(self):
        flor = str(self.especie_flor)+str(self.tamano_flor)
        return flor


flor1= Flor("r","L")
flor2= Flor("g","L")

print(flor1.flor())
print(flor2.flor())

