import pygame
import numpy as np


# from os import path
# dir_path = path.dirname(path.realpath(__file__))

from screeninfo import get_monitors
user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height


# import os
# old_path = os.getcwd()
# new_path = f"{old_path}/"

# from pathlib import Path
# path = Path(new_path)
# new_path = path.parent.absolute()



def load_star_animation():

    # array_of_all_frames = np.zeros(shape = 30)

    # global new_path
    import os
    old_path = os.getcwd()
    new_path = f"{old_path}/"

    from pathlib import Path
    path = Path(new_path)
    new_path = path.parent.absolute()


    star_frames_dummy_surf = pygame.image.load(f"{new_path}/star_frames/1.png").convert_alpha()
    star_frames_dummy_surf = pygame.transform.scale(surface = star_frames_dummy_surf, size = (user_screen_width, user_screen_height))

    array_of_all_frames = np.full((30), star_frames_dummy_surf)

    for frame in range(0, 30):

        # directory = f"{dir_path}/star_frames/" + f"{frame}.png"
        # global new_path
        directory = f"{new_path}/star_frames/{frame}.png"

        current_star_frame_surface = pygame.image.load(directory).convert_alpha()
        current_star_frame_surface = pygame.transform.scale(surface = current_star_frame_surface, size = (user_screen_width, user_screen_height))

        array_of_all_frames[frame] = current_star_frame_surface



    return