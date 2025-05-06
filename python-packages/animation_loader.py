import pygame
from screeninfo import get_monitors
# import os
import numpy as np

import settings

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.init()

list_of_all_frames = []

def load_and_rescale_EVERYTHING(dir_path):
    load_and_rescale_colours(dir_path)
        # pass: add more animations in here in the future if needed!
    return


def load_and_rescale_colours(dir_path):

    user_screen_width = get_monitors()[0].width
    user_screen_height = get_monitors()[0].height

    path = f"{dir_path}/graphics/animations/blend modes/flickering/red/0.png"   # Sample element to initialize the array :3

    colour_flickering_dummy_surf_raw = pygame.image.load(path).convert_alpha()
    colour_flickering_dummy_surf = pygame.transform.scale(surface = colour_flickering_dummy_surf_raw, size = (user_screen_width, user_screen_height))

    
    global list_of_all_frames
    list_of_all_frames = np.full((7, 55), colour_flickering_dummy_surf)
    
    colour_index = -1

    for colour in ("red", "orange", "yellow", "green", "blue", "purple", "black"):     # black will be added in the future, for the final boss... e.e

        colour_index += 1

        for frame in range(0, 55):
            
            path = f"{dir_path}/graphics/animations/blend modes/flickering/" + colour + f"/{frame}.png"

            colour_flickering_surface_raw = pygame.image.load(path).convert_alpha()
            colour_flickering_surface = pygame.transform.scale(surface = colour_flickering_surface_raw, size = (user_screen_width, user_screen_height))

            list_of_all_frames[colour_index][frame] = colour_flickering_surface

    print("everything loaded n ready, captain!! We have humongous amounts of frames loaded right now :3 teehee~")

    return


def frame_blit(number):

    # print(settings.colour_being_hovered_over_by_the_player)

    if settings.colour_being_hovered_over_by_the_player == "none":
        print('You should NOT be seeing this message ingame ":3')
        return

    # print("Problematic colour:", settings.colour_being_hovered_over_by_the_player)
    index = (("red", "orange", "yellow", "green", "blue", "purple", "black").index(settings.colour_being_hovered_over_by_the_player))

    # print("index:", index)

    global list_of_all_frames
    screen.blit(list_of_all_frames[index][number], (0, 0))

    return

"""
def load_and_rescale_background_animation(dir_path):

    pass

    return
"""