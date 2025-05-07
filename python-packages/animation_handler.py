from math import floor, ceil
import animation_loader
import colour_collider_handler
import pygame
import os
from screeninfo import get_monitors

import settings

animation_timer_1 = 0
animation_timer_2 = 0
# step_1 = 0
step_acum_1 = 0
flickering_animation_counter = 0
is_flickering_ascending = True      # Could alternatively just save the immediately previous value for flickering_animation_counter anyway :p



# dir_path = os.path.dirname(os.path.realpath(__file__))

user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height




red_alpha_value = 0
yellow_alpha_value = 0
orange_alpha_value = 0
green_alpha_value = 0
blue_alpha_value = 0
purple_alpha_value = 0


red_title_alpha_value = 0
yellow_title_alpha_value = 0
orange_title_alpha_value = 0
green_title_alpha_value = 0
blue_title_alpha_value = 0
purple_title_alpha_value = 0




silhouette_radio = 3 / 8        # (intended width, intended height) == (screen width / (3 / 8), screen_width)

red_bg_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/red/background.png").convert()
red_bg_surface = pygame.transform.scale(surface = red_bg_surface_raw, size = (user_screen_width, user_screen_height))
red_bg_surface.set_alpha(red_alpha_value)       # Goes from 0 to 255 :3

red_silhouettes_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/red/silhouettes.png").convert_alpha()
red_silhouettes_surface = pygame.transform.scale(surface = red_silhouettes_surface_raw, size = (user_screen_width / silhouette_radio, user_screen_width))
red_silhouettes_surface.set_alpha(red_alpha_value)       # Goes from 0 to 255 :3

red_title_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/red/title.png").convert_alpha()
red_title_surface = pygame.transform.scale(surface = red_title_surface_raw, size = (user_screen_width, user_screen_height))
red_title_surface.set_alpha(red_title_alpha_value)       # Goes from 0 to 255 :3

orange_bg_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/orange/background.png").convert()
orange_bg_surface = pygame.transform.scale(surface = orange_bg_surface_raw, size = (user_screen_width, user_screen_height))
orange_bg_surface.set_alpha(orange_alpha_value)       # Goes from 0 to 255 :3

orange_silhouettes_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/orange/silhouettes.png").convert_alpha()
orange_silhouettes_surface = pygame.transform.scale(surface = orange_silhouettes_surface_raw, size = (user_screen_width / silhouette_radio, user_screen_width))
orange_silhouettes_surface.set_alpha(orange_alpha_value)       # Goes from 0 to 255 :3

orange_title_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/orange/background.png").convert_alpha()
orange_title_surface = pygame.transform.scale(surface = orange_title_surface_raw, size = (user_screen_width, user_screen_height))
orange_title_surface.set_alpha(orange_title_alpha_value)       # Goes from 0 to 255 :3

yellow_bg_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/yellow/background.png").convert()
yellow_bg_surface = pygame.transform.scale(surface = yellow_bg_surface_raw, size = (user_screen_width, user_screen_height))
yellow_bg_surface.set_alpha(yellow_alpha_value)       # Goes from 0 to 255 :3

yellow_silhouettes_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/yellow/silhouettes.png").convert_alpha()
yellow_silhouettes_surface = pygame.transform.scale(surface = yellow_silhouettes_surface_raw, size = (user_screen_width / silhouette_radio, user_screen_width))
yellow_silhouettes_surface.set_alpha(yellow_alpha_value)       # Goes from 0 to 255 :3

yellow_title_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/yellow/title.png").convert_alpha()
yellow_title_surface = pygame.transform.scale(surface = yellow_title_surface_raw, size = (user_screen_width, user_screen_height))
yellow_title_surface.set_alpha(yellow_title_alpha_value)       # Goes from 0 to 255 :3

green_bg_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/green/background.png").convert()
green_bg_surface = pygame.transform.scale(surface = green_bg_surface_raw, size = (user_screen_height, user_screen_height))
green_bg_surface.set_alpha(green_alpha_value)       # Goes from 0 to 255 :3

green_silhouettes_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/green/background.png").convert_alpha()
green_silhouettes_surface = pygame.transform.scale(surface = green_silhouettes_surface_raw, size = (user_screen_width / silhouette_radio, user_screen_width))
green_silhouettes_surface.set_alpha(green_alpha_value)       # Goes from 0 to 255 :3

green_title_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/green/title.png").convert_alpha()
green_title_surface = pygame.transform.scale(surface = green_title_surface_raw, size = (user_screen_width, user_screen_height))
green_title_surface.set_alpha(green_title_alpha_value)       # Goes from 0 to 255 :3

blue_bg_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/blue/background.png").convert()
blue_bg_surface = pygame.transform.scale(surface = blue_bg_surface_raw, size = (user_screen_width, user_screen_height))
blue_bg_surface.set_alpha(blue_alpha_value)       # Goes from 0 to 255 :3

blue_silhouettes_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/blue/silhouettes.png").convert_alpha()
blue_silhouettes_surface = pygame.transform.scale(surface = blue_silhouettes_surface_raw, size = (user_screen_width / silhouette_radio, user_screen_width))
blue_silhouettes_surface.set_alpha(blue_alpha_value)       # Goes from 0 to 255 :3

blue_title_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/blue/title.png").convert_alpha()
blue_title_surface = pygame.transform.scale(surface = blue_title_surface_raw, size = (user_screen_width, user_screen_height))
blue_title_surface.set_alpha(blue_title_alpha_value)       # Goes from 0 to 255 :3

purple_bg_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/purple/background.png").convert()
purple_bg_surface = pygame.transform.scale(surface = purple_bg_surface_raw, size = (user_screen_width, user_screen_height))
purple_bg_surface.set_alpha(purple_alpha_value)       # Goes from 0 to 255 :3

purple_silhouettes_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/purple/silhouettes.png").convert_alpha()
purple_silhouettes_surface = pygame.transform.scale(surface = purple_silhouettes_surface_raw, size = (user_screen_width / silhouette_radio, user_screen_width))
purple_silhouettes_surface.set_alpha(purple_alpha_value)       # Goes from 0 to 255 :3

purple_title_surface_raw = pygame.image.load("graphics/animations/regional_backgrounds/purple/title.png").convert_alpha()
purple_title_surface = pygame.transform.scale(surface = purple_title_surface_raw, size = (user_screen_width, user_screen_height))
purple_title_surface.set_alpha(purple_title_alpha_value)       # Goes from 0 to 255 :3

##### Note: It is intended for bgs and silhouettes to share the same alpha value ---> {colour}_alpha_value.

bg_surface_raw = pygame.image.load("graphics/map_barebone_no_text.png").convert_alpha()
bg_surface = pygame.transform.scale(surface = bg_surface_raw, size = (user_screen_width, user_screen_height))

stellardefenders_surface_raw = pygame.image.load("graphics/world_map.png").convert_alpha()
stellardefenders_surface = pygame.transform.scale(surface = stellardefenders_surface_raw, size = (user_screen_width, user_screen_height))

map_without_names_surface_raw = pygame.image.load("graphics/map_without_region_names.png").convert_alpha()
map_without_names_surface = pygame.transform.scale(surface = map_without_names_surface_raw, size = (user_screen_width, user_screen_height))

region_names_surface_raw = pygame.image.load("graphics/region_names_without_map.png").convert_alpha()
region_names_surface = pygame.transform.scale(surface = region_names_surface_raw, size = (user_screen_width, user_screen_height))




title_surface = pygame.image.load("graphics/text.png").convert_alpha()

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





sfx_0 = pygame.mixer.Sound("audio/SFX/0.wav")
sfx_1 = pygame.mixer.Sound("audio/SFX/1.wav")
sfx_2 = pygame.mixer.Sound("audio/SFX/2.wav")
sfx_3 = pygame.mixer.Sound("audio/SFX/3.wav")
sfx_4 = pygame.mixer.Sound("audio/SFX/4.wav")









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


black_surface_alpha_value = 0           # To be used later on in worldmap_fadeout() and fadeout_to_renpy()
black_surface = pygame.Surface((user_screen_width, user_screen_height), pygame.SRCALPHA)


# sea_timer = 0

sea_bg_surface = pygame.Surface((user_screen_width, user_screen_height))
sea_bg_surface.fill((36, 148, 159))       # Solid colour as background for the sea is #24949f :3



def animation_handler(screen, tick_counter: int, just_animating_colour: bool):
    
    seconds = tick_counter / 60

    match settings.game_state:
        case 0:

            draw_solid_sea_colour(screen)
            draw_animated_seas(screen)


            if just_animating_colour == False:
                
                
                if (seconds) < 9:
                    screen.blit(bg_surface, (0, 0))
                    screen.blit(title_surface, (title_x_pos, title_y_pos))
                    screen.blit(stellardefenders_surface, (0, 0))

                    settings.dont_blit_text = True
                
                else:
                    screen.blit(map_without_names_surface, (0, 0))


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

                elif ((seconds >= 6) & ((seconds) < 9)):
                    stellardefenders_surface.set_alpha(stellardefenders_alpha_value)       # Goes from 0 to 255 :3

                    if (seconds == 6):
                        pygame.mixer.music.play(loops = -1, fade_ms = 1500)     # Fade-in of 90 frames (at 60fps) :3 

                    if (seconds < 7.5):
                        stellardefenders_animation_fadein(90)
                        
                    
            elif settings.colour_being_hovered_over_by_the_player != "none":
                if settings.player_has_just_clicked == True:
                    # seconds = 727     # <--- whatever number you put in here, it should reset to 0 anyway :3 (debugging strategy lol)
                    
                    import region_warper

                    print("COLOUR THAT WILL GET PRINTED TO NEXUS.TXT:", settings.colour_being_hovered_over_by_the_player)
                    region_warper.set_warp_to(settings.colour_being_hovered_over_by_the_player)

                    settings.game_state = 1     # With this implementation there will be a 1-frame delay here between the player clicking a region and the animations playing, but oh well... whatever ":3
                    #print('yay, game_state is 1')

                    

                screen.blit(map_without_names_surface, (0, 0))

                global flickering_animation_counter
                global is_flickering_ascending

                if flickering_animation_counter == 54:               # It will now start going down through the list of frames!
                    is_flickering_ascending = False
                    
                elif flickering_animation_counter == 0:
                    is_flickering_ascending = True

                show_colour_flickering(flickering_animation_counter)

                if is_flickering_ascending == True:
                    flickering_animation_counter += 1
                else:
                    flickering_animation_counter -= 1




            if settings.dont_blit_text == False:
                screen.blit(region_names_surface, (0, 0))

            settings.dont_blit_text = False      # Resets the "dont_blit_text" flag in settings.py :p
                              
            # else:
                # print('how tf did u get here o_o warn the dev!!!! "^^')
        


        case 1:

            screen.blit(settings.screenshot, (0, 0))

            # global black_surface_alpha_value
            # if black_surface_alpha_value >= 250:
                # pass


            # print("play regional background anim lol")
            if seconds == 0:
                play_clicking_SFX()
                pygame.mixer.music.fadeout(floor(102 * 16.666666))      # Fade out for as long as the world map is fading out (So, in this case: time = 102 frames :p)
                

            if (seconds >= 0) & (tick_counter < 102) :   #  (255 / 5) * 2 = 51 * 2 = 102. That is, worldmap_fadeout() lasts for 102 frames :o)
                worldmap_fadeout(tick_counter)

            global black_surface
            screen.blit(black_surface, (0, 0))

            fadeout_start = 443
            fadeout_finish = 173      # The fadeout lasts for 173 frames (I think... lol "^^)
            some_overhead = 2

            if (tick_counter >= 102):
                
                if tick_counter == 102:
                    global black_surface_alpha_value
                    black_surface_alpha_value = 0
                
                    if settings.colour_being_hovered_over_by_the_player == "black":
                        play_extremely_ominous_SFX()

                elif (not (settings.colour_being_hovered_over_by_the_player == "black")):
                    play_ominous_SFX(tick_counter)
                    play_colour_animation(screen, tick_counter)        # play_colour_animation("colour/background", "colour/silhouettes", "colour/title")
                    
                    ######

                    if (tick_counter >= fadeout_start):       
                        fadeout_to_renpy(screen)

                else:
                    print("is this line of code even reachable...? I am interested in knowing this (lol).")

                if (tick_counter > (fadeout_finish + some_overhead)):
                    # settings.warp_to_renpy_region = settings.colour_being_hovered_over_by_the_player
                    pygame.exit()
            




        case _:
            print("ERROR: Invalid game state:", settings.game_state)
            pygame.quit()
            exit()

    # return





def draw_solid_sea_colour(screen):
    screen.blit(sea_bg_surface, (0, 0))       # Solid colour as background for the sea :3

    return



def draw_animated_seas(screen):

    seas_animation()

    sea_rect.bottomleft = (- ceil(truncated_x_pos), (user_screen_height + floor(truncated_y_pos)))
    screen.blit(sea_surface, sea_rect)

    return








sea_surface_raw = pygame.image.load("graphics/animations/map_sea_atlas.png").convert_alpha()
sea_surface = pygame.transform.scale(surface = sea_surface_raw, size = (user_screen_width * 3, user_screen_height * 3))
sea_rect = sea_surface.get_rect(bottomleft = (0, user_screen_height))



slowdown = 5    # slowdown is a float that changes the speed of the sea animation. Write "slowdown = 1" for normal speed. The higher the slowdown, the faster the animation is. The lower the slowdown, the faster the animation is.

step_x = - (16 / slowdown)
step_y = (9 / slowdown)

seas_animation_timer = 0
seas_horizontal_position = 0
seas_vertical_position = 0

truncated_x_pos = 0
truncated_y_pos = 0

def seas_animation():

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



def show_colour_flickering(flickering_animation_counter):
    return animation_loader.frame_blit(flickering_animation_counter)



def play_clicking_SFX():

    sfx_3.play()
    sfx_0.set_volume(settings.sfx_volume)


    return



def play_ominous_SFX(tick_counter):

    match tick_counter:
        case 150:    # 102 + 48
            sfx_0.play()
            sfx_0.set_volume(settings.sfx_volume)

        case 391:   # 102 + 341
            sfx_1.play()
            sfx_1.set_volume(settings.sfx_volume)

        case 487:   # 102 + 385
            sfx_2.play()
            sfx_2.set_volume(settings.sfx_volume)


def play_extremely_ominous_SFX():

    sfx_4.play()
    sfx_4.set_volume(settings.sfx_volume)


    return



def worldmap_fadeout(tick_counter):

    global black_surface_alpha_value
    global black_surface

    if is_even(tick_counter):
        black_surface_alpha_value += 5    # Boo, 30fps animation... lmao
    # black_transition_RGBA = ()
    black_surface.fill((0, 0, 0, black_surface_alpha_value))
    
    return


def is_even(number):
    return (number % 2 == 0)







def play_colour_animation(screen, tick_counter):


    seconds = tick_counter / 60
    # seconds = (tick_counter / 60) - 9 


    # play_colour_animation("orange/background", "orange/silhouettes", "orange/title")
    # screen.blit(colour_background)


    


    index = (("red", "orange", "yellow", "green", "blue", "purple", "black").index(settings.colour_being_hovered_over_by_the_player))
    match index:
        case 0:

            global red_alpha_value
            global red_title_alpha_value

            # if (tick_counter >= 102) & (tick_counter < 208):     # We start after worldmap_fadeout(), and we end when yellow_alpha_value = 104
            if (tick_counter >= 102) & (red_alpha_value < 255 - ceil(settings.bg_and_silhouettes_animation_speed)):
                red_alpha_value += settings.bg_and_silhouettes_animation_speed                # <--- Will finish in frame #(102 + (255/settings.bg_and_silhouettes_animation_speed))
                
            # elif (tick_counter >= 298) & (tick_counter < 400):      
            if (red_title_alpha_value < 255 - ceil(settings.title_animation_speed)):      # For an animation of 102 ticks, we can increase the opacity of the title by 1 every 2 ticks :P
                red_title_alpha_value += floor(settings.title_animation_speed * 2)                       # <--- Will finish in frame #(102 + (255/settings.title_animation_speed))

            global red_bg_surface
            global red_silhouettes_surface
            global red_title_surface

            
            red_bg_surface.set_alpha(red_alpha_value)
            red_silhouettes_surface.set_alpha(red_alpha_value)
            red_title_surface.set_alpha(red_title_alpha_value)



            # It will look more natural if I don't start it at (0, 0), right? :p
            settings.silhouette_x_pos -= 9
            settings.silhouette_y_pos -= 3

            screen.blit(red_bg_surface, (0, 0))
            screen.blit(red_silhouettes_surface, (settings.silhouette_x_pos, settings.silhouette_y_pos))
            screen.blit(red_title_surface, (0, 0))



        case 1:

            global orange_alpha_value
            global orange_title_alpha_value

            # if (tick_counter >= 102) & (tick_counter < 208):     # We start after worldmap_fadeout(), and we end when yellow_alpha_value = 104
            if (orange_alpha_value < 255 - ceil(settings.bg_and_silhouettes_animation_speed)):
                orange_alpha_value += floor(settings.bg_and_silhouettes_animation_speed * 2)               # <--- Will finish in frame #(102 + (255/settings.bg_and_silhouettes_animation_speed))
                
            # elif (tick_counter >= 298) & (tick_counter < 400):      
            if (is_even(tick_counter)) & (orange_title_alpha_value < 255 - ceil(settings.title_animation_speed)):      # For an animation of 102 ticks, we can increase the opacity of the title by 1 every 2 ticks :P
                orange_title_alpha_value += settings.title_animation_speed                       # <--- Will finish in frame #(102 + (255/settings.title_animation_speed))

            global orange_bg_surface
            global orange_silhouettes_surface
            global orange_title_surface

            
            orange_bg_surface.set_alpha(orange_alpha_value)
            orange_silhouettes_surface.set_alpha(orange_alpha_value)
            orange_title_surface.set_alpha(orange_title_alpha_value)



            # It will look more natural if I don't start it at (0, 0), right? :p
            settings.silhouette_x_pos -= 9
            settings.silhouette_y_pos -= 3

            screen.blit(orange_bg_surface, (0, 0))
            screen.blit(orange_silhouettes_surface, (settings.silhouette_x_pos, settings.silhouette_y_pos))
            screen.blit(orange_title_surface, (0, 0))


        case 2:

            global yellow_alpha_value
            global yellow_title_alpha_value

            # if (tick_counter >= 102) & (tick_counter < 208):     # We start after worldmap_fadeout(), and we end when yellow_alpha_value = 104
            if (tick_counter >= 102) & (yellow_alpha_value < 255 - ceil(settings.bg_and_silhouettes_animation_speed)):
                yellow_alpha_value += settings.bg_and_silhouettes_animation_speed                # <--- Will finish in frame #(102 + (255/settings.bg_and_silhouettes_animation_speed))
                
            # elif (tick_counter >= 298) & (tick_counter < 400):      
            if (yellow_title_alpha_value < 255 - ceil(settings.title_animation_speed)):      # For an animation of 102 ticks, we can increase the opacity of the title by 1 every 2 ticks :P
                yellow_title_alpha_value += floor(settings.title_animation_speed * 2)                       # <--- Will finish in frame #(102 + (255/settings.title_animation_speed))

            global yellow_bg_surface
            global yellow_silhouettes_surface
            global yellow_title_surface

            
            yellow_bg_surface.set_alpha(yellow_alpha_value)
            yellow_silhouettes_surface.set_alpha(yellow_alpha_value)
            yellow_title_surface.set_alpha(yellow_title_alpha_value)




            # It will look more natural if I don't start it at (0, 0), right? :p
            settings.silhouette_x_pos -= 9
            settings.silhouette_y_pos -= 3

            screen.blit(yellow_bg_surface, (0, 0))
            screen.blit(yellow_silhouettes_surface, (settings.silhouette_x_pos, settings.silhouette_y_pos))
            screen.blit(yellow_title_surface, (0, 0))


        case 3:

            global green_alpha_value
            global green_title_alpha_value

            # if (tick_counter >= 102) & (tick_counter < 208):     # We start after worldmap_fadeout(), and we end when yellow_alpha_value = 104
            if (tick_counter >= 102) & (green_alpha_value < 255 - ceil(settings.bg_and_silhouettes_animation_speed)):
                green_alpha_value += settings.bg_and_silhouettes_animation_speed                # <--- Will finish in frame #(102 + (255/settings.bg_and_silhouettes_animation_speed))
                
            # elif (tick_counter >= 298) & (tick_counter < 400):      
            if (green_title_alpha_value < 255 - ceil(settings.title_animation_speed)):      # For an animation of 102 ticks, we can increase the opacity of the title by 1 every 2 ticks :P
                green_title_alpha_value += floor(settings.title_animation_speed * 2)                       # <--- Will finish in frame #(102 + (255/settings.title_animation_speed))

            global green_bg_surface
            global green_silhouettes_surface
            global green_title_surface

            
            green_bg_surface.set_alpha(green_alpha_value)
            green_silhouettes_surface.set_alpha(green_alpha_value)
            green_title_surface.set_alpha(green_title_alpha_value)



            # It will look more natural if I don't start it at (0, 0), right? :p
            settings.silhouette_x_pos -= 9
            settings.silhouette_y_pos -= 3

            screen.blit(green_bg_surface, (0, 0))
            screen.blit(green_silhouettes_surface, (settings.silhouette_x_pos, settings.silhouette_y_pos))
            screen.blit(green_title_surface, (0, 0))



        case 4:

            global blue_alpha_value
            global blue_title_alpha_value

            # if (tick_counter >= 102) & (tick_counter < 208):     # We start after worldmap_fadeout(), and we end when yellow_alpha_value = 104
            if (tick_counter >= 102) & (blue_alpha_value < 255 - ceil(settings.bg_and_silhouettes_animation_speed)):
                blue_alpha_value += settings.bg_and_silhouettes_animation_speed                # <--- Will finish in frame #(102 + (255/settings.bg_and_silhouettes_animation_speed))
                
            # elif (tick_counter >= 298) & (tick_counter < 400):      
            if (is_even(tick_counter)) & (blue_title_alpha_value < 255 - ceil(settings.title_animation_speed)):      # For an animation of 102 ticks, we can increase the opacity of the title by 1 every 2 ticks :P
                blue_title_alpha_value += settings.title_animation_speed                       # <--- Will finish in frame #(102 + (255/settings.title_animation_speed))

            global blue_bg_surface
            global blue_silhouettes_surface
            global blue_title_surface

            
            blue_bg_surface.set_alpha(blue_alpha_value)
            blue_silhouettes_surface.set_alpha(blue_alpha_value)
            blue_title_surface.set_alpha(blue_title_alpha_value)



            # It will look more natural if I don't start it at (0, 0), right? :p
            settings.silhouette_x_pos -= 9
            settings.silhouette_y_pos -= 3

            screen.blit(blue_bg_surface, (0, 0))
            screen.blit(blue_silhouettes_surface, (settings.silhouette_x_pos, settings.silhouette_y_pos))
            screen.blit(blue_title_surface, (0, 0))



        case 5:

            global purple_alpha_value
            global purple_title_alpha_value

            # if (tick_counter >= 102) & (tick_counter < 208):     # We start after worldmap_fadeout(), and we end when yellow_alpha_value = 104
            if (tick_counter >= 102) & (purple_alpha_value < 255 - ceil(settings.bg_and_silhouettes_animation_speed)):
                purple_alpha_value += settings.bg_and_silhouettes_animation_speed                # <--- Will finish in frame #(102 + (255/settings.bg_and_silhouettes_animation_speed))
                
            # elif (tick_counter >= 298) & (tick_counter < 400):      
            if (is_even(tick_counter)) & (purple_title_alpha_value < 255 - ceil(settings.title_animation_speed)):      # For an animation of 102 ticks, we can increase the opacity of the title by 1 every 2 ticks :P
                purple_title_alpha_value += settings.title_animation_speed                       # <--- Will finish in frame #(102 + (255/settings.title_animation_speed))

            global purple_bg_surface
            global purple_silhouettes_surface
            global purple_title_surface

            
            purple_bg_surface.set_alpha(purple_alpha_value)
            purple_silhouettes_surface.set_alpha(purple_alpha_value)
            purple_title_surface.set_alpha(purple_title_alpha_value)

            

            # It will look more natural if I don't start it at (0, 0), right? :p
            settings.silhouette_x_pos -= 9
            settings.silhouette_y_pos -= 3

            screen.blit(purple_bg_surface, (0, 0))
            screen.blit(purple_silhouettes_surface, (settings.silhouette_x_pos, settings.silhouette_y_pos))
            screen.blit(purple_title_surface, (0, 0))



        case _:     # Maybe case for black to be implemented in the future, if needed?
            print("What?")
            pass

    return



def fadeout_to_renpy(screen):       # Lasts for 173 frames (I think... lol)

    alpha_step = 1.47398843931

    global black_surface
    global black_surface_alpha_value            # "alpha_acum" :P

    new_alpha = ceil(black_surface_alpha_value + alpha_step)

    if (new_alpha < 255):
        black_surface_alpha_value += alpha_step     # "alpha_acum" :P

    black_surface.fill((0, 0, 0, black_surface_alpha_value))    
    screen.blit(black_surface, (0, 0))


    return




def scale_rectangle_to_screen_size(rectangle: pygame.Rect):

    print("rectangle left should be 448:", rectangle.left)
    print("rectangle top should be 440:", rectangle.top)
    print("rectangle.height:", rectangle.height)
    print("rectangle.width:", rectangle.width)


    # horizontal_scaling_factor = user_screen_width / rectangle.left
    # vertical_scaling_factor = user_screen_height / rectangle.top

    horizontal_scaling_factor = user_screen_width / 1920            # My game is 1920x1080 native resolution.
    vertical_scaling_factor = user_screen_height / 1080             # My game is 1920x1080 native resolution.


    new_left = rectangle.left * horizontal_scaling_factor
    new_top = rectangle.top * vertical_scaling_factor
    new_width = rectangle.width * horizontal_scaling_factor
    new_height = rectangle.height * vertical_scaling_factor

    # new_rectangle = rectangle.scale_by(horizontal_scaling_factor, vertical_scaling_factor)
    new_rectangle = pygame.Rect(new_left, new_top, new_width, new_height)


    return new_rectangle


black_region_hitbox = pygame.Rect(448, 440, 764, 277)       # I am setting the black hitbox as a simple rectangle between vertices (448, 440) and (1212, 717)
black_region_hitbox = scale_rectangle_to_screen_size(black_region_hitbox)


def colour_handler(screen, tick_counter, mouse_pos):            # Needs the tick counter to check for game state (whether the player is in the world map or not!).   // needs game state to check for postgame (3 possible scenarios: hasn't unlocked black // has unlocked black // is in postgame)

    red_postgame_is_available    = ((not (settings.has_completed_red_postgame))    & (settings.has_completed_black_region))
    orange_postgame_is_available = ((not (settings.has_completed_orange_postgame)) & (settings.has_completed_black_region))
    yellow_postgame_is_available = ((not (settings.has_completed_yellow_postgame)) & (settings.has_completed_black_region))
    green_postgame_is_available  = ((not (settings.has_completed_green_postgame))  & (settings.has_completed_black_region))
    blue_postgame_is_available   = ((not (settings.has_completed_blue_postgame))   & (settings.has_completed_black_region))
    purple_postgame_is_available = ((not (settings.has_completed_purple_postgame)) & (settings.has_completed_black_region))


    # print("Debugging with prints sucks...")

    print("settings.has_completed_yellow_region:", settings.has_completed_yellow_region)
    print("yellow_postgame_is_available:", yellow_postgame_is_available)
    # print()


# Logic for colours other than black is as follows:
# For example, for the red region:
# You can go there if:
#### the red region is unvisited
# OR
##### postgame has been unlocked but not finished


    global black_region_hitbox
    
    mouse_pos_tuple = ((mouse_pos.x_coordinate(), mouse_pos.y_coordinate()))      # Converts mouse_pos from type "Vertex" to type "tuple".

    # print("black_region_hitbox.collidepoint(mouse_pos_tuple):", black_region_hitbox.collidepoint(mouse_pos_tuple))

    if ((black_region_hitbox.collidepoint(mouse_pos_tuple)) & (settings.black_region_is_available) & (not (settings.has_completed_black_region))):
        # print("mouse_pos:", mouse_pos_tuple)
        # print("black_region_hitbox:", (black_region_hitbox.left, black_region_hitbox.top, black_region_hitbox.width, black_region_hitbox.height))

        settings.colour_being_hovered_over_by_the_player = "black"
        animation_handler(screen, tick_counter, just_animating_colour = True)

    elif ((colour_collider_handler.red.is_user_on_colour(mouse_pos)) & ((not (settings.has_completed_red_region)) | (red_postgame_is_available))):        # if red region is unvisited OR postgame has been unlocked but not finished
        settings.colour_being_hovered_over_by_the_player = "red"
        animation_handler(screen, tick_counter, just_animating_colour = True)

    elif ((colour_collider_handler.orange.is_user_on_colour(mouse_pos)) & ((not (settings.has_completed_orange_region)) | (orange_postgame_is_available))):
        settings.colour_being_hovered_over_by_the_player = "orange"
        animation_handler(screen, tick_counter, just_animating_colour = True)

        # play_colour_animation("orange/background", "orange/silhouettes", "orange/title")
        

    elif ((colour_collider_handler.yellow.is_user_on_colour(mouse_pos)) & ((not (settings.has_completed_yellow_region)) | (yellow_postgame_is_available))):
        print("Debugging with prints sucks a LOT...")
        settings.colour_being_hovered_over_by_the_player = "yellow"
        animation_handler(screen, tick_counter, just_animating_colour = True)
    
    elif ((colour_collider_handler.green.is_user_on_colour(mouse_pos)) & ((not (settings.has_completed_green_region)) | (green_postgame_is_available))):
        settings.colour_being_hovered_over_by_the_player = "green"
        animation_handler(screen, tick_counter, just_animating_colour = True)        

    elif ((colour_collider_handler.blue.is_user_on_colour(mouse_pos)) & ((not (settings.has_completed_blue_region)) | (blue_postgame_is_available))):
        settings.colour_being_hovered_over_by_the_player = "blue"
        animation_handler(screen, tick_counter, just_animating_colour = True)
    
    elif ((colour_collider_handler.purple.is_user_on_colour(mouse_pos)) & ((not (settings.has_completed_purple_region)) | (purple_postgame_is_available))):
        settings.colour_being_hovered_over_by_the_player = "purple"
        animation_handler(screen, tick_counter, just_animating_colour = True) 
        
    elif settings.game_state == 0:
        settings.colour_being_hovered_over_by_the_player = "none"

    else:
        print("what are you doing here?!?!? o_o")
        print("game_state:", settings.game_state)

    return