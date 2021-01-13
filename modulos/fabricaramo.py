
import random

class FabricaRamo:
    def __init__(self):
        pass
    
    def obtener_ramos_factibles(self,diseno,flores):
        lista_flores_grandes = {}
        lista_flores_Pequenas = {}
        ramos_factibles = []
        diseno_fabricar = random.choice(diseno)
        
        for clave,valor  in flores.items():
            if clave[1] == 'L':
                lista_flores_grandes[clave[0]] = valor
            else:
                lista_flores_Pequenas[clave[0]] = valor      
        
        print(lista_flores_grandes)     
        
        if diseno_fabricar[1] == 'L':
            #0123456789
            #AL8d9r5t30
            if str(lista_flores_grandes[diseno_fabricar[3]]) <= str(diseno_fabricar[2]):
                print('puedo usar esta flor')

                 
            
    
        #return lista_ramos_factibles
    
    def fabricar_ramo(self,lista_ramos_factibles):
        pass
        #obetener aleatoriamente de la lista ramos factibles que ramo generar
        #return ramo
    
    

    
    