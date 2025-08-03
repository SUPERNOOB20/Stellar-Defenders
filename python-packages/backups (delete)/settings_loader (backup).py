# This module initializes some settings in
# settings.py with nexus.txt values.

# For non-technical users: Let's just
# say it loads your progress and shares it
# with the world map when it opens up :)



import json
import settings
# import os
# current_dir = os.getcwd()


def initialize_region_progress():

    data = load_from_savefile("data.json")
    settings = load_from_savefile("settings.json")
    save_to_file(data)
    save_to_file(settings)

    return

def load_from_savefile(file: str):      # ---> list[bool U float]
    # loads settings and progress from a .json file before loading the world map


    # data = open("nexus.txt", "r")
    # data_dict = {}

    # with open('data.json', 'w') as outfile:
        # json.dump(data_dict, outfile)



    if (file == "data.json"):      # when it's loading "data"
        with open('data.json') as json_file:
            data_dict = json.load(json_file)

    region_progress = []
    for i in range(0, 13):
        print("LINE:", data_dict[i], "         ", "DATA TYPE:", type(data_dict[i]))         #   <--- Debugging
        plain_text_to_be_appended = data_dict[i].replace("\r\n", "")
        region_progress.append(plain_text_to_be_appended)
    

    else:   # when it's loading "settings"
        for i in range(0, 3):
            print("LINE:", data_dict[i], "         ", "DATA TYPE:", type(data_dict[i]))         #   <--- Debugging
            plain_text_to_be_appended = data_dict[i].replace("\r\n", "")
            region_progress.append(plain_text_to_be_appended)


    # print(bool(region_progress[3]))
    return region_progress


def save_to_file(region_progress):
    # settings_file = open("settings.py", "w")

    settings.has_completed_red_region = bool(int(region_progress[0]))
    settings.has_completed_orange_region = bool(int(region_progress[1]))
    settings.has_completed_yellow_region = bool(int(region_progress[2]))
    settings.has_completed_green_region = bool(int(region_progress[3]))
    settings.has_completed_blue_region = bool(int(region_progress[4]))
    settings.has_completed_purple_region = bool(int(region_progress[5]))

    should_black_region_be_available(settings.has_completed_red_region, settings.has_completed_orange_region, settings.has_completed_yellow_region, settings.has_completed_green_region, settings.has_completed_blue_region, settings.has_completed_purple_region)

    settings.has_completed_black_region = bool(int(region_progress[6]))

    settings.has_completed_red_postgame = bool(int(region_progress[7]))
    settings.has_completed_orange_postgame = bool(int(region_progress[8]))
    settings.has_completed_yellow_postgame = bool(int(region_progress[9]))
    settings.has_completed_green_postgame = bool(int(region_progress[10]))
    settings.has_completed_blue_postgame = bool(int(region_progress[11]))
    settings.has_completed_purple_postgame = bool(int(region_progress[12]))

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
        settings.black_region_is_available = True
    return

save_to_settings_file