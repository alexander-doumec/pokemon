from pokemon import Pokemon

class Combat:
    def __init__(self,joueur_pokemon, adversaire_pokemon):
        self.__joueur_pokemon = joueur_pokemon
        self.adversaire_pokemon = adversaire_pokemon
        

    def calculer_degats(self):
        type_adversaire = self.adversaire_pokemon.type
        

class Type:
    """toute les resistance"""

