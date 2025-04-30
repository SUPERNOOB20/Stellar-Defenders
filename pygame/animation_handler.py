from math import floor, ceil
import animation_loader
# from colour_collider_handler import Colliders_Colour, red, orange, yellow, green, blue, purple
import colour_collider_handler
import pygame
import os
from screeninfo import get_monitors
# from stellar_defenders_pygame_module import screen

animation_timer_1 = 0
animation_timer_2 = 0
# step_1 = 0
step_acum_1 = 0
flickering_animation_counter = 0
is_flickering_ascending = True      # Could alternatively just save the immediately previous value for flickering_animation_counter anyway :p



dir_path = os.path.dirname(os.path.realpath(__file__))

user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height


bg_surface_raw = pygame.image.load(f"{dir_path}/graphics/map_barebone_no_text.png").convert_alpha()
bg_surface = pygame.transform.scale(surface = bg_surface_raw, size = (user_screen_width, user_screen_height))

stellardefenders_surface_raw = pygame.image.load(f"{dir_path}/graphics/world_map.png").convert_alpha()
stellardefenders_surface = pygame.transform.scale(surface = stellardefenders_surface_raw, size = (user_screen_width, user_screen_height))

title_surface = pygame.image.load(f"{dir_path}/graphics/text.png").convert_alpha()

title_surface.set_alpha(0)      # Goes from 0 to 255 :3
title_alpha_value = 0           # Goes from 0 to 255 :3

stellardefenders_surface.set_alpha(0)           # Goes from 0 to 255 :3
stellardefenders_alpha_value = 0                # Goes from 0 to 255 :3

title_x_pos = 130
title_y_pos = user_screen_height / 2

if user_screen_height < 1080 & user_screen_width < 1920:        # Detects users who have no money (like me, lol x_x)
    new_width = floor(1315 * 0.6)
    new_height = floor(198 * 0.6)
    title_surface = pygame.transform.scale(surface = title_surface, size = (new_width, new_height))

title_x_pos = 130
title_y_pos = user_screen_height / 2

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

def title_animation_fadeout(duration_in_frames, tick_counter):

    step_1 = (255 / duration_in_frames)

    global step_acum_1
    step_acum_1 -= step_1


    global title_alpha_value
    title_alpha_value = floor(step_acum_1)

    if (tick_counter % 2) == 0:
        global title_x_pos
        title_x_pos += 1

    return

# sea_timer = 0

def animation_handler(screen, tick_counter, colour: str, game_state: int, just_animating_colour):
    match game_state:
        case 0:
            match just_animating_colour:
                case 0:
                    seconds = tick_counter / 60

                    # global sea_timer
                    # if (sea_timer % 180:
                    seas_animation(screen)

                    # sea_timer += 1

                    sea_rect.bottomleft = (- ceil(truncated_x_pos), (user_screen_height + floor(truncated_y_pos)))
                    screen.blit(sea_surface, sea_rect)



                    if (seconds) < 9:

                        screen.blit(bg_surface, (0, 0))
                        screen.blit(title_surface, (title_x_pos, title_y_pos))

                    screen.blit(stellardefenders_surface, (0, 0))

                    title_surface.set_alpha(title_alpha_value)       # Goes from 0 to 255 :3

                    if (seconds < 1.5):
                        title_animation_fadein(90)

                    elif ((seconds >= 1.5) & (seconds < 3)):
                        global step_acum_1
                        step_acum_1 = 255

                    elif ((seconds >= 3) & (seconds < 5)):
                        title_animation_fadeout(120, tick_counter)

                    elif ((seconds >= 5) & (seconds < 6)):
                        step_acum_1 = 0

                    elif ((seconds >= 6) & (seconds < 9)):
                        stellardefenders_surface.set_alpha(stellardefenders_alpha_value)       # Goes from 0 to 255 :3

                        if (seconds == 6):
                            pygame.mixer.music.play(loops = -1, fade_ms = 1500)     # Fade-in of 90 frames (at 60fps) :3 

                        if (seconds < 7.5):
                            stellardefenders_animation_fadein(90)
                        
                    
                case 1:
                    # elif (seconds >= 9):

                        # if colour != "none":

                    global flickering_animation_counter
                    global is_flickering_ascending

                    if flickering_animation_counter == 54:               # It will now start going down through the list of frames!
                        is_flickering_ascending = False
                        
                    elif flickering_animation_counter == 0:
                        is_flickering_ascending = True

                    show_colour_flickering(colour, flickering_animation_counter)

                    if is_flickering_ascending == True:
                        flickering_animation_counter += 1
                    else:
                        flickering_animation_counter -= 1
            
        case 1:
            print("play regional background anim lol")
        case _:
            print("ERROR: Invalid game state:", game_state)
            pygame.quit()
            exit()

    # return

sea_surface_raw = pygame.image.load(f"{dir_path}/graphics/animations/map_sea_atlas.png").convert_alpha()
sea_surface = pygame.transform.scale(surface = sea_surface_raw, size = (user_screen_width * 3, user_screen_height * 3))
sea_rect = sea_surface.get_rect(bottomleft = (0, user_screen_height))

# step_x = -16
# step_y = 9

slowdown = 5    # slowdown is a float that changes the speed of the sea animation. Write "slowdown = 1" for normal speed. The higher the slowdown, the faster the animation is. The lower the slowdown, the faster the animation is.

step_x = - (16 / slowdown)
step_y = (9 / slowdown)

seas_animation_timer = 0
seas_horizontal_position = 0
seas_vertical_position = 0

truncated_x_pos = 0
truncated_y_pos = 0

def seas_animation(screen):

    global step_x
    global step_y
    global seas_animation_timer
    global seas_horizontal_position
    global seas_vertical_position
    global truncated_x_pos
    global truncated_y_pos


    seas_animation_timer += 1      # sea_timer == 3 in the third animation frame, 9 in the ninth animation frame... etc.

    if seas_animation_timer < (240 * slowdown):         # The animation should have 255 frames and always loop before the 256th frame :)        !!!! ---> BE CAREFUL HERE WITH THE SLOWDOWN VALUE: IF IT'S NOT AN INTEGER, USE "floor(240 * slowdown)", BUT BEAR IN MIND THAT THE ANIMATION WON'T LOOP CORRECTLY :c

        seas_horizontal_position -= step_x
        seas_vertical_position += step_y

        truncated_x_pos = (seas_horizontal_position / (1920 / user_screen_width))
        truncated_y_pos = (seas_vertical_position / (1080 / user_screen_height))

    else:

        seas_animation_timer = 0

        seas_horizontal_position = 0
        seas_vertical_position = 0

    return

def show_colour_flickering(colour: str, flickering_animation_counter):
    return animation_loader.frame_blit(colour, flickering_animation_counter)
    
def play_clicking_SFX():
    return

def play_ominous_SFX():
    return

def worldmap_fadeout():
    return

def play_colour_animation(colour_background, colour_silhouettes, colour_title):

    # screen.blit(colour_background)
    play_ominous_SFX()
    return



def colour_handler(screen, tick_counter, mouse_pos, game_state):            # Needs the tick counter to check for game state (whether the player is in the world map or not!).
    
    # if colour_collider_handler.red.is_user_on_colour(mouse_pos):
        # animation_handler(screen, tick_counter, "red", game_state, just_animating_colour = 1)
        # useless_temp_variable = 0

    if colour_collider_handler.orange.is_user_on_colour(mouse_pos):
        animation_handler(screen, tick_counter, "orange", game_state, just_animating_colour = 1)
        play_clicking_SFX()
        worldmap_fadeout()
        # play_colour_animation("orange/background", "orange/silhouettes", "orange/title")
        # print("you is on orange :3")

    elif colour_collider_handler.yellow.is_user_on_colour(mouse_pos):
        animation_handler(screen, tick_counter, "yellow", game_state, just_animating_colour = 1)
        # print("you is on yellow :3")
    
    # elif colour_collider_handler.green.is_user_on_colour(mouse_pos):
        # animation_handler(screen, tick_counter, "green", game_state, just_animating_colour = 1)
        # useless_temp_variable = 0

    # elif colour_collider_handler.blue.is_user_on_colour(mouse_pos):
        # animation_handler(screen, tick_counter, "blue", game_state, just_animating_colour = 1)
        # useless_temp_variable = 0

    # elif colour_collider_handler.purple.is_user_on_colour(mouse_pos):
        # animation_handler(screen, tick_counter, "purple", game_state, just_animating_colour = 1)
        # useless_temp_variable = 0

    return