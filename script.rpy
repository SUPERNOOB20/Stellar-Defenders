# The script of the game goes in this file.

init python:

    import os
    renpy_boot_path = os.getcwd()

    # boot_path_str = str(os.getcwd())
    python_boot_path = f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe"

    import subprocess
    subprocess.run(f"{python_boot_path} animation_init.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/python-scripts/intro_animation")



label splashscreen:

    # $ renpy.movie_cutscene('intro.mp4')
    # $ renpy.movie_cutscene('intro.m2v')
    # $ renpy.movie_cutscene('intro.avi')

    


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

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

#     p "[boot_path_str]"

    # python:
        # import subprocess

        # subprocess.run(r"C:/Users/Claudia/AppData/Local/Programs/Python/Python313/python.exe aux_script.py", cwd = r"D:/non_OS/RenPy/Projects/Stellar Defenders/game")
        # while(True):
            # pass
            # hi = "hello!"

    p ":o"

    stop music

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

        import subprocess
        subprocess.run(f"{renpy_boot_path}/Stellar Defenders/game/pygame/Python312/python.exe stellar_defenders_pygame_module.py", cwd = f"{renpy_boot_path}/Stellar Defenders/game/pygame")

    # This ends the game.

    return
