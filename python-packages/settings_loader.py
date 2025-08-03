# This module loads your progress in "data.json" and your preferences in "settings.json".

# You need this persistent data to go back and forth from RenPy to the world map without losing data. 




import json

import os
print("CURR_DIR:", os.getcwd())
os.chdir("d:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/")
os.chdir("python-packages")

data = {}
config = {}


def load_persistent_data():     # Loads persistent data from storage ("loads the game")

    load_progress()
    load_preferences()

    return

def load_progress():

    global data

    with open("data.json") as json_file:
        data = json.load(json_file)

    return

def load_preferences():

    global config

    with open("settings.json") as json_file:
        config = json.load(json_file)

    return

def save_persistent_data():     # Saves persistent data to storage ("saves the game")

    save_progress()
    save_preferences()

    return

def save_progress():            # Saves player's progress to storage
    
    global data

    with open('data.json', 'w') as outfile:         
        json.dump(data, outfile)                    

    return


def save_preferences():         # Saves player's preferences to storage

    global config

    with open('settings.json', 'w') as outfile:     
        json.dump(config, outfile)

    return

def reset():                # Resets data.json and settings.json

    reset_data()
    reset_settings()

    return



def reset_data():            # Resets data.json
    
    global data

    if len(data) != 0:
        print("Already existing data has been found, are you sure you want to continue?" "Y / N")
    
        if (input() == ("N")):
            return
    
    print("Generating data...")


    #    vv     Game progress settings (NO TOUCHY! >:c)    vv
    data["current_region"] = '-'
    data["has_completed_red_region"] = False         # bool
    data["has_completed_orange_region"] = False      # bool
    data["has_completed_yellow_region"] = False      # bool
    data["has_completed_green_region"] = False       # bool
    data["has_completed_blue_region"] = False        # bool
    data["has_completed_purple_region"] = False      # bool

    data["black_region_is_available"] = False        # bool       <--- Switch to True when debugging (Should, of course, be "False" in new save files).
    data["has_completed_black_region"] = False       # bool

    data["has_completed_red_postgame"] = False       # bool
    data["has_completed_orange_postgame"] = False    # bool
    data["has_completed_yellow_postgame"] = False    # bool
    data["has_completed_green_postgame"] = False     # bool
    data["has_completed_blue_postgame"] = False      # bool
    data["has_completed_purple_postgame"] = False    # bool

    save_progress()

    print("Data generated succesfully :) (exit code: 0)")
    return



def reset_settings():            # Resets settings.json
    
    global config

    if len(config) != 0:
        print("Already existing settings have been found, are you sure you want to continue?" "Y / N")
    
        if (input() == ("N")):
            return
    
    print("Generating settings...")

    #    vv     User experience / adjustable settings - Change to your heart's content :3 (no invalid values pls or I cry)      vv
    config["SFX_volume"] = 0.4000         # float between 0.000 and 1.000 plsss
    config["BGM_volume"] = 1.0000         # float between 0.000 and 1.000 plsss
    config["Show_FPS"] = True
    # config["Fullscreen"] = True         #   <--- I'll implement this someday maybe e.e      //      # Pro tip: Press F11 to switch between Fullscreen and Windowed mode! :3

    save_preferences()

    print("Settings generated succesfully :) (exit code: 0)")
    return






#####   TESTS   #####
if __name__ == "__main__":

    def show_data_and_settings():       #   <--- Debugging


        # Shows data.
        print("--- DATA ---")
        for key, value in data.items():
            print("KEY:", key, "     ", "VALUE:", value, "     ", "DATA TYPE:", type(value))
            
        # Shows settings.
        print("--- SETTINGS ---")
        for key, value in config.items():
            print("KEY:", key, "     ", "VALUE:", value, "     ", "DATA TYPE:", type(value))
            

        return




    def test_0():       
        
        reset_data()
        reset_settings()

        return
    

    def test_1():       # Testea save file nuevo

        global data
        global config

        reset()         # Initializes data.json and settings.json
        data["has_completed_red_region"] = True
        data["has_completed_blue_region"] = True

        return


    def test_2():       # Testea save file nuevo
        
        global data
        global config

        load_progress()
        data["has_completed_yellow_region"] = True

        return


    def test_3():       # Testea save file nuevo
        
        global data

        load_persistent_data()

        data["has_completed_orange_region"] = True
        data["has_completed_green_region"] = True
        data["has_completed_purple_region"] = True

        save_persistent_data()

        return
    

    def test_4():       # Testea save file nuevo
        
        global data
        global config

        reset()

        data["has_completed_orange_region"] = True
        data["has_completed_blue_region"] = True
        config["Show_FPS"] = False
        config["SFX_volume"] = 0.0727
        config["BGM_volume"] = 0.069

        save_persistent_data()

        return


    # ---------------------------------------------------------------------------------------------


    reset()

    """

    print("\n \n \n --- TEST 0 - DEFAULT DATA AND SETTINGS ---")
    test_0()
    show_data_and_settings()

    print("\n \n \n --- TEST 1 ---")
    test_1()
    show_data_and_settings()

    print("\n \n \n --- TEST 2 ---")
    test_2()
    show_data_and_settings()

    print("\n \n \n --- TEST 3 ---")
    test_3()
    show_data_and_settings()

    print("\n \n \n --- TEST 4 ---")
    test_4()
    show_data_and_settings()

    """