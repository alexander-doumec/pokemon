import pygame
import pygame_menu
from typing import Optional
from PIL import Image


FPS = 60 
WINDOW_SIZE = (1080, 800)

sound: Optional['pygame_menu.sound.Sound'] = None
surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None


#recharger l'image 
background_image = pygame_menu.BaseImage(image_path=pygame_menu.baseimage)

#def main_background() -> None :
    