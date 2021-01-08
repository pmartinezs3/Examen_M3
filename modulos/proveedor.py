from flor import Flor

class Proveedor(Flor):
    def __init__(self,especie_flor,tamano_flor):
        self.lista_tipos = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.tamanos = ["S","L"]
    super().__init__()
    
    def generarflores(self,cantidad):
        for i  in range(cantidad):
            print(i)
            
            
flor1 = Proveedor("R","S")

print(dir(Proveedor))
    

        



