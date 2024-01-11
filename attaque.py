types = ["Eau", "Feu", "Plante", "Terre", "Insecte", "Vol", "Dragon", "Glace", "Combat", "Fée", " Psy", "Acier", "Ténèbres", "Fée"]
attaque = [1, 1.5, 0.5, 1, 1, 1.5, 2, 1.5, 1, 1, 1, 0.5, 0.5, 1]
defense = [1, 0.5, 2, 1, 1.5, 0.5, 1, 0.5, 2, 1, 1, 2, 2, 1]

types_to_indices = {
    "Eau": 0,
    "Feu": 1,
    "Plante": 2,
    "Terre": 3,
    "Insecte": 4,
    "Vol": 5,
    "Dragon": 6,
    "Glace": 7,
    "Combat": 8,
    "Fée": 9,
    " Psy": 10,
    "Acier": 11,
    "Ténèbres": 12,
    "Fée": 13
}

def subir_attaque(attaquant, cible, attaque, defense):
    attaquant_index = types_to_indices[attaquant]
    cible_index = types_to_indices[cible]
    facteur_attaque = attaque[attaquant_index]
    facteur_defense = defense[cible_index]
    degats = 10 * facteur_attaque * facteur_defense
    return degats