import pygame
from sys import exit
from math import floor
import os

from screeninfo import get_monitors

from collider_handler import check_colliders
from collider_handler import check_colliders_init


user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

exit_game = False
is_on_fullscreen = True

animation_timer_1 = 0
# step_1 = 0
step_acum_1 = 0



dir_path = os.path.dirname(os.path.realpath(__file__))


icon_surface = pygame.image.load(f"{dir_path}/graphics/icon.png").convert_alpha() 
pygame.display.set_icon(icon_surface)

bg_surface_raw = pygame.image.load(f"{dir_path}/graphics/map_barebone_no_text.png").convert()
title_surface = pygame.image.load(f"{dir_path}/graphics/text.png").convert_alpha()
stellardefenders_surface_raw = pygame.image.load(f"{dir_path}/graphics/map_v4.2.png").convert()
colliders_surface_raw = pygame.image.load(f"{dir_path}/graphics/colliders.png").convert_alpha()
colliders_and_continent_surface_raw = pygame.image.load(f"{dir_path}/graphics/colliders_and_continent.png").convert_alpha()

bg_surface = pygame.transform.scale(surface = bg_surface_raw, size = (user_screen_width, user_screen_height))
stellardefenders_surface = pygame.transform.scale(surface = stellardefenders_surface_raw, size = (user_screen_width, user_screen_height))
colliders_surface = pygame.transform.scale(surface = colliders_surface_raw, size = (user_screen_width, user_screen_height))
colliders_and_continent_surface = pygame.transform.scale(surface = colliders_and_continent_surface_raw, size = (user_screen_width, user_screen_height))

title_surface.set_alpha(0)      # Goes from 0 to 255 :3
title_alpha_value = 0           # Goes from 0 to 255 :3

stellardefenders_surface.set_alpha(0)           # Goes from 0 to 255 :3
stellardefenders_alpha_value = 0        # Goes from 0 to 255 :3

if user_screen_height < 1080 & user_screen_width < 1920:        # Detects users who have no money (like me, lol x_x)
    new_width = floor(1315 * 0.6)
    new_height = floor(198 * 0.6)
    title_surface = pygame.transform.scale(surface = title_surface, size = (new_width, new_height))

title_x_pos = 130
title_y_pos = user_screen_height / 2

clock = pygame.time.Clock()

pygame.display.set_caption("Stellar Defenders")

tick_counter = 0    # How many frames the game has been running for (1 tick = 1 frame)
seconds = 0

mouse_pos_x = 0
mouse_pos_y = 0

class Colliders_Colour:
    def __init__(self, vertices, triangles, center_vertices, center_vertices_plane_region):

        self.vertices = vertices
        self.triangles = triangles
        self.center_vertices = center_vertices
        self.center_vertices_plane_region = center_vertices_plane_region

        # self.name = "Yellow"


    def is_user_on_colour(self):

        result = False

        cv = -1

        for t in self.triangles:

                cv += 1

                mouse_pos_check = check_colliders(t[0], t[1], t[2], self.center_vertices_plane_region[cv], mouse_pos)
                result == True         # ... then the user is in this region! :D
        
        return result


y_v0 = (1114, 421)
y_v1 = (1116, 335)
y_v2 = (1176, 303)
y_v3 = (1213, 167)
y_v4 = (1267, 135)
y_v5 = (1495, 346)

y_t0 = [y_v0, y_v1, y_v2]   # The triangle goes like this: t0 = [v0, v1, v2, v0]. Same reasoning behind all other triangles!
y_t1 = [y_v2, y_v3, y_v4]
y_t2 = [y_v0, y_v4, y_v5]

y_cv0 = (1134, 348)
y_cv1 = (1227, 179)
y_cv2 = (1306, 292)

# center_vertex_plane_region = (bool, bool, bool)
center_vertex_plane_region_0 = check_colliders_init(y_t0[0], y_t0[1], y_t0[2], y_cv0)
center_vertex_plane_region_1 = check_colliders_init(y_t1[0], y_t1[1], y_t1[2], y_cv1)
center_vertex_plane_region_2 = check_colliders_init(y_t2[0], y_t2[1], y_t2[2], y_cv2)


yellow_vertices = [y_v0, y_v1, y_v2, y_v3, y_v4, y_v5]
yellow_triangles = [y_t0, y_t1, y_t2]
yellow_center_vertices = [y_cv0, y_cv1, y_cv2]
yellow_center_vertices_plane_region = [center_vertex_plane_region_0, center_vertex_plane_region_1, center_vertex_plane_region_2]

yellow = Colliders_Colour(yellow_vertices, yellow_triangles, yellow_center_vertices, yellow_center_vertices_plane_region)

# def is_user_on_t1():
# def is_user_on_t2():



# is_user_on_yellow = Colliders_Yellow.is_user_on_t0() | Colliders_Yellow.is_user_on_t1() | Colliders_Yellow.is_user_on_t2()

# check_colliders(Colliders_Yellow.t0, (1134, 348)) | check_colliders(Colliders_Yellow.t1, (1227, 179)) | check_colliders(Colliders_Yellow.t2, (1306, 292))

# if (tick_counter = 540):
#   print(is_user_on_yellow)

# p1 = Person("John", 36)



def stellardefenders_animation_fadein(animation_duration_in_frames):

    step_1 = (255 / animation_duration_in_frames)

    global step_acum_1
    step_acum_1 += step_1

    global stellardefenders_alpha_value
    stellardefenders_alpha_value = floor(step_acum_1)

    return

def title_animation_fadein(animation_duration_in_frames):

    step_1 = (255 / animation_duration_in_frames)

    global step_acum_1
    step_acum_1 += step_1

    global title_alpha_value
    title_alpha_value = floor(step_acum_1)
    
    global title_x_pos
    title_x_pos += 1

    return

def title_animation_fadeout(duration_in_frames):

    step_1 = (255 / duration_in_frames)

    global step_acum_1
    step_acum_1 -= step_1


    global title_alpha_value
    title_alpha_value = floor(step_acum_1)

    if (tick_counter % 2) == 0:
        global title_x_pos
        title_x_pos += 1

    return

import time
time.sleep(4)

pygame.mixer.init()
pygame.mixer.music.load(f"{dir_path}/audio/world_map.mp3")


while True:     # EVERYTHING INSIDE THIS LOOP IS IN THE EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:        # processes all the Keydown events
            if event.key == pygame.K_ESCAPE:    # processes the Escape event (The event that the key 'ESCAPE' is hit!)
                exit_game = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            mouse_pos_x = mouse_pos[0]
            mouse_pos_y = mouse_pos[1]

            print("Is the player clicking on the Yellow region? ", yellow.is_user_on_colour(),
                  "(mouse position is ", mouse_pos, " btw).")

    screen.blit(bg_surface, (0, 0))

    screen.blit(title_surface, (title_x_pos, title_y_pos))
    screen.blit(stellardefenders_surface, (0, 0))

    if exit_game == True:
        pygame.quit()
        exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
        if is_on_fullscreen == False:
            pygame.display.toggle_fullscreen()
            
            is_on_fullscreen = True

            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        else: # is_on_fullscreen == True:
            pygame.display.toggle_fullscreen()

            windowed_width = floor(user_screen_width * 9.5/10)
            windowed_height = floor(user_screen_height * 9/10)

            screen = pygame.display.set_mode((windowed_width, windowed_height), pygame.RESIZABLE)

            is_on_fullscreen = False

    # if tick_counter == 0:   # Runs only the first frame of the game
        # title_animation_init(90, 150, 120)

    if (seconds < 1.5):
        title_animation_fadein(90)

    elif ((seconds >= 1.5) & (seconds < 3)):
        step_acum_1 = 255

    elif ((seconds >= 3) & (seconds < 5)):
        title_animation_fadeout(120)

    elif ((seconds >= 5) & (seconds < 6)):
        step_acum_1 = 0

    elif ((seconds >= 6) & (seconds < 9)):
        stellardefenders_surface.set_alpha(stellardefenders_alpha_value)       # Goes from 0 to 255 :3

        if (seconds == 6):
            print("OK!!!")
            pygame.mixer.music.play(fade_ms = 1500)     # Fade-in of 90 frames (at 60fps) :3 

        if (seconds < 7.5):
            stellardefenders_animation_fadein(90)

    title_surface.set_alpha(title_alpha_value)       # Goes from 0 to 255 :3

    if seconds < 9:
        tick_counter += 1
        seconds = tick_counter / 60

    """
    mouse_pos = pygame.mouse.get_pos()

    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    """

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        screen.blit(colliders_surface, (0, 0))
    elif keys[pygame.K_2]:
        screen.blit(colliders_and_continent_surface, (0, 0))


    # print(tick_counter)
    pygame.display.update()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling