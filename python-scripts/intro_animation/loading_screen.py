import pygame
pygame.init()

# from screen_renderer import render_on_screen, render_fadeout
from screen_renderer import render_fadeout

import os
# print(os.getcwd())
current_path = os.getcwd()


from screeninfo import get_monitors
user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height


loading_screen_surface = pygame.image.load(f"{current_path}\images\loading_screen.png")
loading_screen_surface = pygame.transform.scale(surface = loading_screen_surface, size = (user_screen_width, user_screen_height))




def play_loading_screen(screen):

    # render_on_screen(screen, [loading_screen_surface])
    screen.blit(loading_screen_surface, (0, 0))


    return





def play_fadeout(screen):

    render_fadeout(screen, 90)


    return