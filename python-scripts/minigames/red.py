import os
os.chdir("python-scripts/minigames")

def play_red_minigame():

    from screeninfo import get_monitors
    user_screen_width = get_monitors()[0].width
    user_screen_height = get_monitors()[0].height


    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    bg_surf_raw = pygame.image.load("meteor_rain_bg.png").convert()
    bg_surf = pygame.transform.scale(surface = bg_surf_raw, size = (user_screen_width, user_screen_height))

    pygame.display.toggle_fullscreen()
    while running:

        screen.fill((0, 0, 0))       #   <--- MASSIVE THANKS TO: https://stackoverflow.com/a/68054220

        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # If the user clicks on the X button. Well... they shouldn't be able to, in the first place? But whatever...
                running = False

            if event.type == pygame.KEYDOWN:        # processes all the Keydown events
                if event.key == pygame.K_ESCAPE:    # processes the Escape event (The event that the key 'ESCAPE' is hit!)
                    running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((0, 0, 0))       #   <--- MASSIVE THANKS TO: https://stackoverflow.com/a/68054220

        screen.blit(bg_surf, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60






play_red_minigame()