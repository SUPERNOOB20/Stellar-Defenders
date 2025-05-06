import pygame
pygame.init()

from math import floor



# def render_on_screen(screen = pygame.display.set_mode, surfaces_to_render = list[pygame.surface.Surface]):
# def render_on_screen(screen, surfaces_to_render):

  #   for surf in surfaces_to_render:
    #     screen.blit(surf, (0, 0))

        
    # return




"""
def render_on_screen(screen = pygame.display.set_mode, surfaces_to_render = list[pygame.Surface]):

    for surf in surfaces_to_render:

        if (type(surf) == pygame.Surface):
            print("ta todo bien")
            screen.blit(surf, (0, 0))

        else:
            print("type(surf):", type(surf))
            # print("render error, baka! :p")
            return
            


    return
"""




def render_fadeout(screen = pygame.display.set_mode, frames = int):

    black_screen_alpha_value = 0    # Goes between 0 and 255, of course :p
    alpha_step = 255 / frames       # Figures out the alpha value increase black_surface should have so that the animation lasts for the requested amount of frames~  :3                    # before: 256 / frames

    black_screen_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    
    

    frames_into_the_fadeout: int = 0

    clock = pygame.time.Clock()

    while frames_into_the_fadeout < frames:
        # print("alpha value:", black_screen_alpha_value)
        # print("alpha value floor:", floor(black_screen_alpha_value))
        black_screen_surface.fill((0, 0, 0, floor(black_screen_alpha_value)))
        screen.blit(black_screen_surface)

        black_screen_alpha_value += alpha_step 

        frames_into_the_fadeout += 1

        pygame.display.flip()
        # screen.fill((0,0,0))
        clock.tick(60)  # Caps the events loop at a 60fps ceiling

    black_screen_alpha_value = 0    # Resets the value to the initial one.
    return




# pygame.quit()