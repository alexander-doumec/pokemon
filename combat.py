
from pokemon import Pokémon

class Combat: 
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1 
        self.pokemon2 = pokemon2
        

    def effectuer_attaque(self, attaquant, defenseur):
        #attaque 
        degats = attaquant.puissance_attaque - defenseur.defense
        degats = max(degats, 0) #les degats ne peuvent pas etre négatifs 
        
        #appliquer les degats aux points de vie du défenseur 
        
        defenseur.points_de_vie -= degats 
        
        print(f"{attaquant.nom} attaque {defenseur.nom} et lui inflige {degats} points de vie de dêgats.")
        
        def determiner_gagnant(self):
            if self.pokemon1.pv <= 0:
                return self.pokemon2
            elif self.pokemon2.pv <=0:
                return self.pokemon1
            else:
                return None #aucun gagnant le combat continue 
            
        def simuler_combat(self):
            print(f"Combat entre {self.pokemon1.nom} et {self.pokemon2.nom} commence!")
            
            while True:
                #Alternance desd attaques entre les deux pokemon
                self.effectuer_attaque(self.pokemon1, self.pokemon2)
                gagnant = self.determiner_gagnant()
                if gagnant:
                    print(f"{gagnant.nom} a gagné le combat!")
                    break
                
#fonctions pour charger les pokémons depuis un fichier JSON 