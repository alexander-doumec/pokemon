import pygame  
import pygame_menu  


pygame.init()

width, heigth = 800, 600 
window = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Menu avec Pygame Menu")

#definir les couleurs 
blanc = (255, 255, 255)
noir = (0, 0, 0)

#fonction a exécuter lorsque le bouton jouer esr cliqué
def start_game():
    print("Lancement du Jeu !")

#création du menu 
menu = pygame_menu.Menu("Pygame Menu", width, heigth, theme=pygame_menu.themes.THEME_DARK)

"Ajout des boutons Jouer avec action associé et quitter pour fermer le menu"
menu.add.button("Jouer", start_game)

menu.add.button("Quitter", pygame_menu.events.EXIT)

#charger l'image de fond 
image_fond = pygame_menu.BaseImage('image/pokeball.jpg', drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)

#Appliquer l'image de fond au menu 
menu.set_background_image(image_fond, alpha=0.5)

#Boucle principale
    #effacer l'écran
while True:
    window.fill(blanc)

    #traiter les evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Afficher le menu
    menu.mainloop(window)
    #mettre a jour l'affichage
    pygame.display.flip()