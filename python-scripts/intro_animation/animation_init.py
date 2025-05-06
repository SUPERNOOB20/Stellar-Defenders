from loading_screen import play_loading_screen, play_fadeout
from intro import play_intro
from animation_loader import load_star_animation


import pygame
pygame.init()


from screeninfo import get_monitors
user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height

screen = pygame.display.set_mode((user_screen_width, user_screen_height))

play_loading_screen(screen)
load_star_animation()
play_fadeout(screen)
play_intro(screen)
