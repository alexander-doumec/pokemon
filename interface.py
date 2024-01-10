import pygame
pygame.init()

#generer la fenetre de notre jeu 

pygame.display.set_caption("Pokemon")
screen = pygame.display.set_mode((1280,1024))

#importer l'image pour charger l'arriere plan de notre jeu 
background = pygame.image.load('image/fond.jpg')

running = True

#boucle tant que condition est vrai 
while running:
    #appliquer l'arriere plan de notre jeu 
    screen.blit(background, (0,0))

    #mettre à jour l'écran 
    pygame.display.flip()

    #si le joueur ferme la fenetre 
    for event in pygame.event.get():
        #verifier que l'evenement est fermeture de fenetre 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")