import pygame
pygame.init()

# from screen_renderer import render_on_screen, render_fadeout
from screen_renderer import render_fadeout

from screeninfo import get_monitors
user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height
print("size?", user_screen_width, user_screen_height)


screen = pygame.display.set_mode((user_screen_width, user_screen_height))




import os
old_path = os.getcwd()
new_path = f"{old_path}/images/"
os.chdir(new_path)






panel_1_surface_raw = pygame.image.load("panel_1.png").convert()        # Feel fry to try with convert_alpha() instead if the visuals are glitchy.
panel_1_surface = pygame.transform.scale(surface = panel_1_surface_raw, size = (user_screen_width, user_screen_height))

panel_2_surface_raw = pygame.image.load("panel_2.png").convert()        # Feel fry to try with convert_alpha() instead if the visuals are glitchy.
panel_2_surface = pygame.transform.scale(surface = panel_2_surface_raw, size = (user_screen_width, user_screen_height))

print("debugging:", user_screen_width, user_screen_height)


tick_counter: int = 0   # It's a frame counter. I'm initializing it at 0.


def play_intro(screen):

    global tick_counter
    global panel_1_surface
    global panel_2_surface

    clock = pygame.time.Clock()

    while tick_counter < 470:

        screen.fill((0,0,0))

        if ((tick_counter >= 40) & (tick_counter <= 174)):
            # render_on_screen(screen, [panel_1_surface])
            screen.blit(panel_1_surface, (0, 0))

            if tick_counter == 174:        

                fadeout_duration_in_frames = 138

                render_fadeout(screen, frames = fadeout_duration_in_frames)
                tick_counter += fadeout_duration_in_frames
        


        elif ((tick_counter >= 40) & (tick_counter < 392)):    # When (tick_counter < 392):
            # render_on_screen(screen, [panel_2_surface])
            screen.blit(panel_2_surface, (0, 0))

            if (tick_counter == 392):
                
                fadeout_duration_in_frames = 72

                render_fadeout(screen, frames = fadeout_duration_in_frames)
                tick_counter += fadeout_duration_in_frames




        tick_counter += 1

        pygame.display.flip()
        # screen.fill((0,0,0))
        clock.tick(60)  # Caps the events loop at a 60fps ceiling
        

    return