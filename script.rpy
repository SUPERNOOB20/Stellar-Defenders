# The script of the game goes in this file.

init python:

    import os
    renpy_boot_path = os.getcwd()

    import settings
    print(settings.game_state)

    # world_map_handler_directory = "/Stellar Defenders/game/pygame/"
    # os.chdir(renpy_boot_path + world_map_handler_directory)

    # main_module_directory = os.getcwd()
    
    
    
    # from world_map_handler import start_world_map
    # import world_map_handler
    
    
    
    
    # os.chdir(renpy_boot_path)

    python_boot_path = f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe"

    import subprocess

    DETACHED_PROCESS = 0x00000008

    subprocess.run(f"{python_boot_path} animation_init.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-scripts/intro_animation", creationflags = DETACHED_PROCESS)



label splashscreen:
    # put some sick ass white fadeout here, heh :3
    return






# Declares characters used by this game. The color argument colorizes the...
# ...name of the character.

define p = Character("Phoebe")
define r = Character("Rhea")
define n = Character("Noon")
define am = Character("Amaru")
define h = Character("Hector")
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

    # python:
        # import subprocess

        # subprocess.run(r"C:/Users/Claudia/AppData/Local/Programs/Python/Python313/python.exe aux_script.py", cwd = r"D:/non_OS/RenPy/Projects/Stellar Defenders/game")
        # while(True):
            # pass
            # hi = "hello!"

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


        
        import subprocess
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)


        renpy_normal_path = os.getcwd()






        # file = renpy.open_file(fn = "nexus.txt", directory = f"{renpy_boot_path}/Stellar Defenders/game/python-packages/nexus.txt")
        file = renpy.open_file(fn = 'nexus.txt', encoding = "utf-8", directory = "/python-packages/")
        
        # line_0 = file[0]
        
        colour_picked_by_the_player = "ola"

        dummy_counter = 0
        for line in file:
            if (dummy_counter == 0):
                colour_picked_by_the_player = line
                dummy_counter += 1


        
        
        # print(colour_picked_by_the_player)
        
        colour_picked_by_the_player.replace("\r\n", "")
        



    p "you have finished the world map... ha"
    # p "let's see... you picked region [current_colour], is that correct? (^-^)"
    # p "let's see... you picked region [file], is that correct?"
    # p "haha nahhh jk... it's [line_0], isn't it? (^-^)"
    # p "You have entered the [line_0] region... right? (^-^)"
    p "You have entered the [colour_picked_by_the_player] region... right? (^-^)"
    p "if not... weeeeeell... you might wanna warn SUPERNOOB :p"
    p "alright, let's send you there...!"
    # p "alright, end of the demo"
    # p "see you around! Now get outta here :p"



    return

#     renpy.full_restart()
    
jump colour_picked_by_the_player


label red:
    "This is the red region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

label orange:
    "This is the orange region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

label yellow:
    "This is the yellow region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

label green:
    "This is the green region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

label blue:
    "This is the blue region :p"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

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
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

    # This ends the game.

    "End of the demo. Thank you so much for playing!"
    "Bye byeeee, see you around :3)/"


label black:
    "This is the black region :O"

    p "let's say you've completed this region, or whatever."

    p "you'll be going back to the worldmap now :) magic!"

    python:
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe world_map_handler.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-packages", creationflags = DETACHED_PROCESS)

    return
