class Pokemon:
    def __init__(self, nom, pv, niveau, puissance_attaque, defense):
        self.__nom = nom 
        self.__pv = pv 
        self.__niveau = niveau 
        self.__puissance_attaque = puissance_attaque
        self.__defense = defense

    def get_nom(self):
        return self.__nom 
    
    def set_nom(self, nom):
        self.__nom = nom 

    def get_pv(self):
        return self.__pv
    
    def set_pv(self, pv):
        self.__pv = pv 

    def get_niveau(self): 
        return self.__niveau 
    
    def set_niveau(self, niveau):
        self._niveau = niveau 

    def get_puissance_attaque(self):
        return self.__puissance_attaque
    
    def set_puissance_attaque(self, puissance_attaque):
        self.__puissance_attaque = puissance_attaque

    def get_defense(self):
        return self.__defense
    
    def set_defense(self, defense):
        self.__defense = defense