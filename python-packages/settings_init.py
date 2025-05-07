# This module initializes some settings in
# settings.py with nexus.txt values.

# For non-technical users: Let's just
# say it loads your progress and sends it
# to the world map when it opens up :)

import settings
import os
current_dir = os.getcwd()


def initialize_region_progress():

    progress = load_from_nexus()
    save_to_settings_file(progress)

    return

def load_from_nexus() -> list[bool]:

    global current_dir
    nexus_textfile = open(f"{current_dir}/python-packages/nexus.txt", "r")
    # nexus_textfile = open("/python-packages/nexus.txt", "r")
    nexus_file = nexus_textfile.readlines()

    region_progress = []
    for i in range(1, 16):
        region_progress.append(nexus_file[i])

    return region_progress


def save_to_settings_file(region_progress):
    # settings_file = open("settings.py", "w")

    settings.has_completed_red_region = bool(region_progress[0])
    settings.has_completed_orange_region = bool(region_progress[1])
    settings.has_completed_yellow_region = bool(region_progress[2])
    settings.has_completed_green_region = bool(region_progress[3])
    settings.has_completed_blue_region = bool(region_progress[4])
    settings.has_completed_purple_region = bool(region_progress[5])

    should_black_region_be_available(settings.has_completed_red_region, settings.has_completed_orange_region, settings.has_completed_yellow_region, settings.has_completed_green_region, settings.has_completed_blue_region, settings.has_completed_purple_region)

    settings.has_completed_black_region = bool(region_progress[6])

    settings.has_completed_red_postgame = bool(region_progress[7])
    settings.has_completed_orange_postgame = bool(region_progress[8])
    settings.has_completed_yellow_postgame = bool(region_progress[9])
    settings.has_completed_green_postgame = bool(region_progress[10])
    settings.has_completed_blue_postgame = bool(region_progress[11])
    settings.has_completed_purple_postgame = bool(region_progress[12])

    settings.sfx_volume = float(region_progress[13])
    settings.bgm_volume = float(region_progress[14])

    return



def should_black_region_be_available(red, orange, yellow, green, blue, purple):
    
    # red = bool(red)
    # orange = bool(orange)
    # yellow = bool(yellow)
    # green = bool(green)
    # blue = bool(blue)
    # purple = bool(purple)


    if (red & orange & yellow & green & blue & purple):
        settings.has_completed_black_region = True
    return
