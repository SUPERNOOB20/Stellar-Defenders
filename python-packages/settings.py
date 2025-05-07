# vv       INTERNAL SETTINGS - PLEASEEEEE NO TOUCHY D:         vv

game_state: int = 0
colour_being_hovered_over_by_the_player = "none"
player_has_just_clicked: bool = 0
dont_blit_text: bool = 0
screenshot = "I will store screenshots here :3 uwu"

# ---------------------------------------------------------------------------------
#                                                                                 |
# Rational number between 0 and 255.                                              |
# Represents the alpha step between each frame :3 uwu                             |
# Bigger number = more speed. Lower number = less speed!!! :]                     |
#                                                                                 |
#                                                                                 |
bg_and_silhouettes_animation_speed = 2       #                                    |
title_animation_speed = 2                    #                                    |
#                                                                                 |                                    
# ---------------------------------------------------------------------------------

silhouette_x_pos = 0
silhouette_y_pos = 0




warp_to_renpy_region = "TESTTTTTTTT"
attempt_to_keep_the_game_running: bool = 1







#    vv     Game progress settings     vv

has_completed_red_region: bool = 0
has_completed_orange_region: bool = 0
has_completed_yellow_region: bool = 0
has_completed_green_region: bool = 0
has_completed_blue_region: bool = 0
has_completed_purple_region: bool = 0

black_region_is_available: bool = 0        # <--- Switch to 1 when debugging (Should, of course, be "0" in new save files).
has_completed_black_region: bool = 0

has_completed_red_postgame: bool = 0
has_completed_orange_postgame: bool = 0
has_completed_yellow_postgame: bool = 0
has_completed_green_postgame: bool = 0
has_completed_blue_postgame: bool = 0
has_completed_purple_postgame: bool = 0



# vv       user experience / adjustable settings - Change to your heart's content :3 (no invalid values pls or I cry)         vv

sfx_volume = 0.4000        # between 0.000 and 1.000 plsss
bgm_volume = 1.0000

show_fps: bool = 1
# fullscreen = 1         # Pro tip: Press F11 to switch between Fullscreen and Windowed mode! :3