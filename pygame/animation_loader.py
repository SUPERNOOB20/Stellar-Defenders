import pygame
from screeninfo import get_monitors
import os

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.init()

list_of_all_frames = []

def load_and_rescale_EVERYTHING(dir_path):

    user_screen_width = get_monitors()[0].width
    user_screen_height = get_monitors()[0].height

    

    for frame in range(0, 55):
        for colour in ("red", "orange", "yellow", "green", "blue", "purple"):     # black will be added in the future, for the final boss... e.e
            path = f"{dir_path}/graphics/animations/blend modes/flickering/" + colour + f"/{frame}.png"

            # print("Is it working? current frame being loaded: ", flickering_animation_counter)

            colour_flickering_surface_raw = pygame.image.load(path).convert_alpha()
            colour_flickering_surface = pygame.transform.scale(surface = colour_flickering_surface_raw, size = (user_screen_width, user_screen_height))

            global list_of_all_frames
            list_of_all_frames.append(colour_flickering_surface)

    return

def frame_blit(colour, number):

    colour_factor = ((("red", "orange", "yellow", "green", "blue", "purple").index(colour)) + 1)

    index = colour_factor + number

    global list_of_all_frames
    screen.blit(list_of_all_frames[index], (0, 0))

    return