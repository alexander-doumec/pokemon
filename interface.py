import pygame
import sys

pygame.init()

lageur_fenetre = 600
hauteur_fenetre = 400
fenetre = pygame.display.set_mode((lageur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Pokémon")

#Couleurs

blanc = (255, 255, 255)
rouge = (255, 0, 0)

#Police

police = pygame.font.Font(None, 36)

#Fonction pour afficher le texte sur le bouton
def afficher_texte_bouton(texte, couleur, position):
    texte_surface = police.render(texte, True, couleur)
    text_rect = texte_surface.get_rect(center=position)
    fenetre.blit((texte_surface, text_rect))
    
#boucle principale

while True:
    fenetre.fill(blanc)
    
    #gestion des évenements
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            #verifications des clic sur le bouton 
            if 100 < x < 300 and 120 < y < 100:
                print("Jouer")
                #code pour lancer le jeu
                
            elif 100 < x < 300 and 100 < y < 170:
                print("Pokedex")
                #mettre le code pour affciher le pokédex
            
            elif 100 < x < 300 and 190 < y < 240:
                print("Quitter")
                pygame.quit()
                sys.exit()
                
#afficher les boutons 

    pygame.draw.rect(fenetre, noir, (100, 50, 200, 50))
    afficher_texte_bouton("Jouer, ")
                 