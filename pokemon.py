class Pokémon :
    def __init__(self, nom, pv, niveau, puissance_attaque, defense, type):
        self.nom = nom 
        self.pv = pv 
        self.niveau = niveau 
        self.puissance_attaque = puissance_attaque
        self.defense = defense 
        self.type = type 
        
    def afficher_informations(self):
        print(f"Nom : {self.nom}")
        print(f"Points de vie :  {self.pv}")
        print(f"Niveau : {self.niveau}")
        print(f"Puissance d'attaque: {self.puissance_attaque}")
        print(f"Défense: {self.defense}")
        print(f"Type : {self.type }")