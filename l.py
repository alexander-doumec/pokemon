import pygame as pg

# Initialisation de Pygame
pg.init()

# Création de la fenêtre
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Arrière-plan avec image")

# Chargement de l'image en arrière-plan
background = pg.image.load('image.png')

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Dessin de l'image en arrière-plan
    screen.blit(background, (0, 0))

    # Mise à jour de l'affichage
    pg.display.flip()

# Fermeture de Pygame
pg.quit()