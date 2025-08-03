# vv       INTERNAL SETTINGS - PLEASEEEEE NO TOUCHY D:         vv

game_state: int = 0
colour_being_hovered_over_by_the_player: str = "none"
player_has_just_clicked: bool = False
dont_blit_text: bool = False
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
attempt_to_keep_the_game_running: bool = True







#    vv     Game progress settings (NO TOUCHY! >:c)    vv

progress = {
"has_completed_red_region": False,         # bool
"has_completed_orange_region": False,      # bool
"has_completed_yellow_region": False,      # bool
"has_completed_green_region": False,       # bool
"has_completed_blue_region": False,        # bool
"has_completed_purple_region": False,      # bool

"black_region_is_available": False,        # bool       <--- Switch to True when debugging (Should, of course, be "False" in new save files).
"has_completed_black_region": False,       # bool

"has_completed_red_postgame": False,       # bool
"has_completed_orange_postgame": False,    # bool
"has_completed_yellow_postgame": False,    # bool
"has_completed_green_postgame": False,     # bool
"has_completed_blue_postgame": False,      # bool
"has_completed_purple_postgame": False     # bool
}





#    vv     User experience / adjustable settings - Change to your heart's content :3 (no invalid values pls or I cry)      vv

settings = {
"sfx_volume": 0.4000,          # float between 0.000 and 1.000 plsss
"bgm_volume": 1.0000,          # float between 0.000 and 1.000 plsss

"show_fps": True               # bool

# fullscreen = 1               # Pro tip: Press F11 to switch between Fullscreen and Windowed mode! :3
}