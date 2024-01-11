import pygame
import os
pygame.init()

#on creer la fenetre 
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon")

#variable du jeu 

game_paused = False

background = pygame.image.load(os.path.join('image/fond.jpg'))

#font 
font = pygame.font.SysFont("arialblack", 40)

#couleurs

TEXT_COL = (255, 255, 255)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:
    screen.fill((52, 78, 91))

    screen.blit(background, (0,0))
    #check si le jeu est en pause 
    if  game_paused == True:
        pass
    else:
        draw_text("Tapez espace pour mettre en Pause", font, TEXT_COL, 300, 150)
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.QUIT()