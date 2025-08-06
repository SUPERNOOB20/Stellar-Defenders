# The script of the game goes in this file.

init python:

    import os
    import json

    renpy_boot_path = config.gamedir

    # os.chdir(f"{renpy_boot_path}/Stellar Defenders/game")

    path_dict = {"path": renpy_boot_path}

    with open('path.json', 'w') as outfile:         
        json.dump(path_dict, outfile)               # SAVES path.json AT "\renpy-8.3.7-sdk\Stellar Defenders\game\python-packages"
                                                    # path.json WILL LOOK LIKE THIS: "..\\renpy-8.3.7-sdk\\Stellar Defenders\\game"

    import settings
    print(settings.game_state)

    import settings_loader
    settings_loader.load_persistent_data()

    import subprocess

    DETACHED_PROCESS = 0x00000008

    # Here a is the array holding the objects
    # passed as the argument of the function

    # import sys
    # print(file=sys.stderr)


    # subprocess.run("pythonw.exe animation_init.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-scripts/intro_animation", creationflags = DETACHED_PROCESS)

    import logging

    os.chdir(r"D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-scripts/intro_animation")
    # subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-scripts/intro_animation"', creationflags = DETACHED_PROCESS)

    new_path = os.getcwd()

    new_path_dict = {"path": new_path}

    with open('newpath.json', 'w') as outfile:         
        json.dump(new_path_dict, outfile)               # SAVES path.json AT "D:\non_OS\renpy-8.3.7-sdk\Stellar Defenders\game\python-scripts\intro_animation"
                                                    # path.json WILL LOOK LIKE THIS: "D:\non_OS\renpy-8.3.7-sdk\Stellar Defenders\game\python-scripts\intro_animation"


    try:
        subprocess.run('python.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-scripts/intro_animation/animation_init.py"', shell = True, capture_output = True)
    except Exception as msg:
    # except subprocess.CalledProcessError.stderr as msg
        logging.error(msg)     #writes in log file
        with open('python_subprocess_errors.txt', 'w') as file:
            file.write(msg)
            file.close()

    # subprocess.run(r'pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-scripts/intro_animation"')


    
    os.chdir(r"D:/non_OS/renpy-8.3.7-sdk/")



label splashscreen:
    # put some sick ass white fadeout here, heh :3
    return






# Declares characters used by this game. The color argument colorizes the...
# ...name of the character.

define p  = Character("Phoebe")
define r  = Character("Rhea")
define n  = Character("Noon")
define am = Character("Amaru")
define h  = Character("Hector")
define cy = Character("Cybele")
define ch = Character("Chun Min-min")
define ar = Character("Ariadne")

# image bg map = Movie(play="SD_map_sea_animation.mp4", side_mask=True)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg map

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show phoebe happy

    # These display lines of dialogue.

    # p "You've created a new Ren'Py game."

    # p "Once you add a story, pictures, and music, you can release it to the world!"

    # p "This is the directory RenPy is importing from ---> " + "[renpy_boot_path]"

    p "[renpy_boot_path]"

    "Once upon a time..."
    "...a very handsome individual was fated to save the world..."
    p "...and uhhh..."
    p 'oh! H-hi there "^^'

    stop music

    p "Welcome to the demo!"
    p "Let's test some stuff and see if it works properly, shall we? ^-^"
    p "I will take you to the world map now :3"

    python:

        # vv Leaving this bit of code here just in case I need it at some point lol sorryyyy "^^
        # world_map_handler.start_world_map()


        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        # subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        # subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"')

        try:
            subprocess.run('python.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', shell = True, capture_output = True)
        except Exception as msg:
        # except subprocess.CalledProcessError.stderr as msg
            logging.error(msg)     #writes in log file
            with open('python_subprocess_errors.txt', 'w') as file:
                file.write(msg)
                file.close()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

        # renpy_normal_path = os.getcwd()

    p "you have finished the world map... ha"

    python:
    
        settings_loader.load_persistent_data()

        colour_picked_by_the_player = "ola"
        
        # os.getcwd()       # current path: \renpy-8.3.7-sdk\
        # curr_dir = os.chdir('/Stellar Defenders/game/python-packages/')

        colour_picked_by_the_player = settings_loader.data["current_region"]        # <--- WHAT PATH IS IT LOADING THIS FROM???
        
        colour_picked_by_the_player.replace("\r\n", "")


    # p "let's see... you picked region [current_colour], is that correct? (^-^)"
    # p "let's see... you picked region [file], is that correct?"
    # p "haha nahhh jk... it's [line_0], isn't it? (^-^)"
    # p "You have entered the [line_0] region... right? (^-^)"
    p "You have entered the <<[colour_picked_by_the_player]>> region... right? (^-^)"
    p "if not... weeeeeell... you might wanna warn SUPERNOOB :p"
    # p "tell him that I just looked at <<[curr_dir]>>! >:c"
    p "alright, let's send you there...!"
    # p "alright, end of the demo"
    # p "see you around! Now get outta here :p"

    jump expression colour_picked_by_the_player

    # return

#     renpy.full_restart()



label red:
    "This is the red region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 1, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_red_region"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label orange:
    "This is the orange region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 2, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_orange_region"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label yellow:
    "This is the yellow region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 3, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_yellow_region"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label green:
    "This is the green region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 4, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_green_region"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label blue:
    "This is the blue region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 5, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_blue_region"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label purple:
    "This is the purple region :p"

    menu talking_to_ariadne:
        "What is it?"
        "Is there anyone you don't really like?":
            ar "..."
            p "..."


    menu talking_to_ariadne_2:
        # DEPRECATED: "Is there anything I can help you with?"
        "How can I help?"
        "What is this place?":
            # none of your business (ha)
            ar "It\'s a library. The largest one in all of Irisum"
        "Why is your hair so long":
            ar "M-my... hair?"
            p "Yeah!"
            ar "U-ummm... well..."
            ar "I... don\'t have time to cut it, ok! ><"
            p "Uh... ok, fair enough"
            p "(Geez...)"
            p "(I wonder if she \'doesn\'t have time\' to shower either?)"
            p "(Gross...)"
        "what about Teseo?":
            ar "That filthy scum, son of a harpy!!!"
            p "!!!"
            ar "-eek!"
            ar "Sorry... e.e"
            ar "He... I'll never forgive him :("
            p "What's wrong with him?"
            ar "I... I used to live in Crete, did you know...?"
            ar "But then [i]that[i] stuff happened, and, ummm..."
            ar "..."
            p "...and now you're here."
            ar "...and now I'm here, yes."
            p "Would you go back home, if you could?"
            ar "No."
            ar "I have gotten wind of my father's assassination."
            ar "There's no home for me in Crete anymore."
            ar "..."
            p "..."
            ar "At any rate..."
            ar "...there's plenty of books here! :D"
            ar "Wherever I can read and drink tea, that is an upright home for me ^-^"
            p "Awesome! ^-^"
        "who is your God?":
            ar "My... god?"
            ar "Well... we have a lot of gods, you know"
            p "Ah... right \"^^"
            ar "Sometimes I wonder if the gods have abandoned me..."
            ar "Maybe it is my fate... to sorrow in solitude..."
            
            menu comforting_answer:
                "Don\'t say that...":
                    ar "..."
                "You are not in solitude, I am here by your side":
                    ar "..."

        

    p "ok"

    ar "ok"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 6, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_purple_region"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

    # This ends the game.

    "End of the demo. Thank you so much for playing!"
    "Bye byeeee, see you around :3)/"


label black:
    "This is the black region :O"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 7, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_black_region"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

    # return

label red_postgame:

    p "This is the red postgame."

    p "let's say you just finished this part..."

    p "You will go back to the world map now :3"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 8, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_red_postgame"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")
    
label orange_postgame:
    p "This is the red postgame."

    p "let's say you just finished this part..."

    p "You will go back to the world map now :3"

    python:
        
        # change_specified_line_in_a_txt_file("nexus.txt", 9, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_orange_postgame"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label yellow_postgame:

    p "This is the red postgame."

    p "let's say you just finished this part..."

    p "You will go back to the world map now :3"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 10, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_yellow_postgame"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label green_postgame:

    p "This is the red postgame."

    p "let's say you just finished this part..."

    p "You will go back to the world map now :3"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 11, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_green_postgame"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")

label blue_postgame:

    p "This is the red postgame."

    p "let's say you just finished this part..."

    p "You will go back to the world map now :3"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 12, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)
        
        settings_loader.data["has_completed_blue_postgame"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")
        

label purple_postgame:

    p "This is the red postgame."

    p "let's say you just finished this part..."

    p "You will go back to the world map now :3"

    python:
        # change_specified_line_in_a_txt_file("nexus.txt", 13, 1)
        # subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python313/pythonw.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

        settings_loader.data["has_completed_purple_postgame"] = True
        settings_loader.save_progress()

        os.chdir("D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages")
        subprocess.run('pythonw.exe "D:/non_OS/renpy-8.3.7-sdk/Stellar Defenders/game/python-packages/world_map_handler.py"', creationflags = DETACHED_PROCESS)
        os.chdir("D:/non_OS/renpy-8.3.7-sdk/")


    return
return