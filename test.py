__all__ = ['main']

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Optional

#constantes de la fenetre
FPS = 60
WINDOW_SIZE = (1080 , 800)

sound: Optional['pygame_menu.sound.Sound'] = None
surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None

# charger l'image en fond
background_image = pygame_menu.BaseImage(
    image_path='pokeball.jpg'
)


def main_background() -> None:
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    background_image.draw(surface)


def main(test: bool = False) -> None:
    """
    Main program.

    :param test: Indicate function is being tested
    """
    global main_menu
    global sound
    global surface

    # création de la fenetre
    surface = create_example_window( 'POKEMON', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # Create menus: Main menu
    main_menu_theme = pygame_menu.themes.THEME_ORANGE.copy()
    main_menu_theme.set_background_color_opacity(0.5)  # 50% opacity

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        onclose=pygame_menu.events.EXIT,  # PEUT UTILISER LA TOUCHE ECHAP POUR QUITTER
        theme=main_menu_theme,
        title='Menu',
        width=WINDOW_SIZE[0] * 0.5
    )
#application de l'image de fond lorsqu'on appuie sur la premiere rubrique 
    theme_bg_image = main_menu_theme.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path='background.jpg'
    )

    #on configure la rubrique commencer
    theme_bg_image.title_font_size = 25
    menu_with_bg_image = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='Commencer',
        width=WINDOW_SIZE[0] * 0.8
    )
    #on configure ce que l'on peut trouver dans la rubrique "commencer"
    menu_with_bg_image.add.button('Retour', pygame_menu.events.BACK)

#on configure la taille de nos onglets
    widget_colors_theme = pygame_menu.themes.THEME_ORANGE.copy()
    widget_colors_theme.widget_margin = (0, 10)
    widget_colors_theme.widget_padding = 0
    widget_colors_theme.widget_selection_effect.margin_xy(10, 5)
    widget_colors_theme.widget_font_size = 20
    widget_colors_theme.set_background_color_opacity(0.5)  # 50% opaque
    widget_colors_theme.set_background_image(image_path='background.jpg')
#on creer la rubrique pokédex lorqu'on appuie sur le celui-ci 
    widget_colors = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        theme=widget_colors_theme,
        title='Pokédex',
        width=WINDOW_SIZE[0] * 0.8
    )

    button_image = pygame_menu.BaseImage(pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER)

    widget_colors.add.button('Opaque color button',
                             background_color=(100, 100, 100))
   

    main_menu.add.button('Commencer', menu_with_bg_image)
    main_menu.add.button('Pokédex', widget_colors)
    main_menu.add.button('Another fancy button', lambda: print('This button has been pressed'))
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # Main loop
    while True:

        # Tick
        clock.tick(FPS)

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()