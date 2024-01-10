from Button import button
import pygame

class gamestage:
    def __init__(self,bgImage,window, initialX, initialY,stage):
        self.bgImage = bgImage
        self.window = window
        self.bgCoords = [initialX,initialY]
        self.stage = stage
        self.width = 600
        self.height = 600

    def mainMenu(self, paleLavander, lightRed , green,event):
        mouse = pygame.mouse.get_pos()
        playButton = button(self.window,paleLavander,75,480,100,50,"PLAY")
        moreButton = button(self.window,paleLavander,425,480,100,50,"MORE")

        playButton.draw()
        moreButton.draw()

        if playButton.hover(mouse):
            playButton.color = green
            playButton.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stage = "createPlayer"

        if moreButton.hover(mouse):
            moreButton.color = green
            moreButton.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stage = "optionsMenu"

    def optionsMenu(self, paleLavander, lightRed, green , event):
        mouse = pygame.mouse.get_pos()

        controlsButton = button(self.window,paleLavander,45,240,100,50,"CTRLS")
        returnButton = button(self.window,paleLavander,45,430,100,50,"BACK")

        controlsButton.draw()
        returnButton.draw()

        if controlsButton.hover(mouse):
            controlsButton.color = green
            controlsButton.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stage = "controlsMenu"

        if returnButton.hover(mouse):
            returnButton.color = green
            returnButton.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stage = "mainMenu"

    # IT IS MISSING THE OPTION OF CHANGING THE CONTROLS!!!!!!!!
    def controlsMenu(self,paleLavander,lightRed,green,event):
        mouse = pygame.mouse.get_pos()

        arrowsImage = pygame.transform.scale(pygame.image.load('image/background.jpg'),(150,100))
        wasdImage = pygame.transform.scale(pygame.image.load('image/pokeball.jpg'),(150,100))

        self.window.blit(arrowsImage,(75,300))
        self.window.blit(wasdImage,(375,300))

        returnButton = button(self.window, paleLavander, 450,500,100,50,"BACK")
        returnButton.draw()

        if returnButton.hover(mouse):
            returnButton.color = green
            returnButton.draw()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stage = "optionsMenu"

    def game(self,event):
        keys = pygame.key.get_pressed()
        self.bgImage = pygame.image.load('images/backgrounds/map.png')