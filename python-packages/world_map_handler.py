# IMPORTANT: RENPY INITIALIZES THIS FROM FOLDER /python-packages/ ---> KEEP THIS IN MIND WHEN HANDLING OS STUFF

import pygame       # Imports pygame-ce
from sys import exit
from math import floor
import os

from screeninfo import get_monitors
user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height

from animation_handler import animation_handler, colour_handler
from geometry import Vertex

import settings


import settings_loader

settings_loader.load_persistent_data()

#   vv    If the player has completed all regions, unlock the final region.    vv
if (settings_loader.data["has_completed_red_region"] & settings_loader.data["has_completed_orange_region"] & settings_loader.data["has_completed_yellow_region"] & settings_loader.data["has_completed_green_region"] & settings_loader.data["has_completed_blue_region"] & settings_loader.data["has_completed_purple_region"]):
        settings_loader.data["black_region_is_available"] = True 



# ----------------------------------------------------------------------------------------------------------------------------


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

exit_game = False
is_on_fullscreen = True




dir_path = os.path.dirname(os.path.realpath(__file__))


icon_surface = pygame.image.load("graphics/icon.png").convert_alpha() 
pygame.display.set_icon(icon_surface)


title_surface = pygame.image.load("graphics/text.png").convert_alpha()
stellardefenders_surface_raw = pygame.image.load("graphics/world_map.png").convert_alpha()
colliders_surface_raw = pygame.image.load("graphics/colliders.png").convert_alpha()
colliders_and_continent_surface_raw = pygame.image.load("graphics/colliders_and_continent.png").convert_alpha()

stellardefenders_surface = pygame.transform.scale(surface = stellardefenders_surface_raw, size = (user_screen_width, user_screen_height))
colliders_surface = pygame.transform.scale(surface = colliders_surface_raw, size = (user_screen_width, user_screen_height))
colliders_and_continent_surface = pygame.transform.scale(surface = colliders_and_continent_surface_raw, size = (user_screen_width, user_screen_height))

# title_surface.set_alpha(0)      # Goes from 0 to 255 :3
# title_alpha_value = 0           # Goes from 0 to 255 :3

stellardefenders_surface.set_alpha(0)           # Goes from 0 to 255 :3
stellardefenders_alpha_value = 0                # Goes from 0 to 255 :3

clock = pygame.time.Clock()

pygame.display.set_caption("Stellar Defenders")

tick_precounter = 0     # Used for loading screen ":3
tick_counter = 0        # How many frames the game has been running for (1 tick = 1 frame)
seconds = 0

# import time           # <--- put loading screen here yo lazy a55 ":3
# time.sleep(4)

pygame.mixer.init()
pygame.mixer.music.load("audio/music/world_map.mp3")
pygame.mixer.music.set_volume(settings_loader.config["BGM_volume"])

def Render_Text(what, color, where):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)

    return



while True:                                                    # EVERYTHING INSIDE THIS LOOP IS IN THE EVENT LOOP
# while settings.attempt_to_keep_the_game_running:                 # EVERYTHING INSIDE THIS LOOP IS IN THE EVENT LOOP

    screen.fill((0, 0, 0))       #   <--- MASSIVE THANKS TO: https://stackoverflow.com/a/68054220

    for event in pygame.event.get():

        
        #       vv   DEBUGGING    vv

        """
        if __name__ == "__main__":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print("mouse_pos when you clicked:", mouse_pos)
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            settings.player_has_just_clicked = True

        if event.type == pygame.QUIT:
            settings_loader.save_persistent_data()
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:        # processes all the Keydown events
            if event.key == pygame.K_ESCAPE:    # processes the Escape event (The event that the key 'ESCAPE' is hit!)
                exit_game = True

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
    
    match settings.game_state:
        case 0:

            if tick_precounter == 0:

                loading_screen_surface_raw = pygame.image.load("graphics/loading_screen.png")
                loading_screen_surface = pygame.transform.scale(surface = loading_screen_surface_raw, size = (user_screen_width, user_screen_height))

                screen.blit(loading_screen_surface, (0, 0))

                pygame.font.init()
                my_font = pygame.font.SysFont('arial', 72)

                text_surface = my_font.render('Loading...', True, (255, 0, 255))


                screen.blit(text_surface, ((user_screen_width * (7.5/10)), user_screen_height * (8.25/10)))

                tick_precounter += 1

            elif (tick_precounter == 1) & (seconds == 0):

                import animation_loader
                animation_loader.load_and_rescale_EVERYTHING(dir_path)

                print("Bulky animations initialized succesfully :)")

                tick_precounter += 1

            else:


                animation_handler(screen, tick_counter, just_animating_colour = False)     # Think of it as a "timeline" in video editing software! :3


                if seconds < 9:
                    tick_counter += 1
                    seconds = tick_counter / 60

                else:

                    mouse_pos = pygame.mouse.get_pos()

                    mouse_pos_x = mouse_pos[0]
                    mouse_pos_y = mouse_pos[1]

                    mouse_pos_vertex = Vertex(mouse_pos_x, mouse_pos_y)



                    #     vv    DEBUGGING    vv
                    # mouse_pos_vertex = Vertex(570, 300)

                    colour_handler(screen, tick_counter, mouse_pos_vertex)


                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    screen.blit(colliders_surface, (0, 0))
                elif keys[pygame.K_2]:
                    screen.blit(colliders_and_continent_surface, (0, 0))
                    


            # settings.colour_being_hovered_over_by_the_player = "none"            
            
        case 1: 

            if (seconds == 9):          # Resets the timeline when the player has just clicked on a region.
                tick_counter = 0
                seconds = 0
            
            animation_handler(screen, tick_counter, just_animating_colour = False) 
            
            tick_counter += 1
            
        case _:
            pass


    if (
        (settings.colour_being_hovered_over_by_the_player != "none") &
        (settings.player_has_just_clicked == True) &
        (settings.game_state == 1)
        ):

        # seconds = 727     # <--- whatever number you put in here, it should reset to 0 anyway :3 (debugging strategy lol)
        # print('yay, game_state is 1')
        # print('Taking a screenshot of the screen ("frame freeze")')
        settings.screenshot = pygame.Surface(screen.get_size())         # Could also have used pygame.Surface(user_screen_width, user_screen_height)...
        settings.screenshot.blit(screen, (0, 0))


    settings.player_has_just_clicked = False
    
    if settings_loader.config["Show_FPS"] == True:
        pygame.font.init()
        try:
            Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
            # print("FPS:", int(clock.get_fps()))
        except:
            pass


    try:
        pygame.display.flip()
        # pygame.display.update()
    except:
        pass


    try:
        clock.tick(60)  # Caps the events loop at a 60fps ceiling
    except:
        pass
