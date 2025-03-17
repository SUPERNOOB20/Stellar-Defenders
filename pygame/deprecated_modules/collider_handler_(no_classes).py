# About the "check_colliders()" function: It receives "(v1, v2, vA, vC)", where:

# v1 is vertex 1. Format must be: v1 = (x1_coordinate, y1_coordinate)
# v2 is vertex 2 Format must be: v2 = (x2_coordinate, y2_coordinate)
# vA is an arbitrary vertex: a point inside the region to be detected! Format must be: vA = (xA_coordinate, yA_coordinate)
# vC is the vertex to check if it's inside the region or not... you usually want this one to be the mouse position :3 ---> vC = (mouse_x_pos, mouse_y_pos)

# ------------------------------------------------

# from this library you will need to import "check_colliders_init" and "check_colliders"

# What the code does is:
# set_game_resolution() needs to be given the original width and height of your game/project. In my case, it's 1920x1080, but the user may play my game in a smaller screen or in a bigger screen, so this function resizes their mouse_pos to 1920x1080 :3
# check_colliders_init() needs to be given the 3 vertices of your triangle AND a vertex inside the triangle. It returns the (bool, bool, bool) combination for your triangle. Useful to calculate the collider preemptively, outside event loops!
# check_colliders() needs to be given (v0, v1, v2, check_colliders_init(), vC), where vC is the vertex of the player position or cursor position that you want to check is inside the triangle or not :)

# The way the code works is... it finds the (bool, bool, bool) combination for vA, then the (bool, bool, bool) combination for vC.
# If the (bool, bool, bool) combinations are the same, the player is inside the triangle, and returns True. Otherwise, the player is outside the triangle, so it returns False.

# ------------------------------------------------

# Returns "is_cursor_inside",
from screeninfo import get_monitors
from math import floor

user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height

game_width = 0
game_height = 0

def set_game_resolution(width, height):
    global game_width
    global game_height

    game_width = width
    game_height = height
    return

def finds_line_equation(v1, v2):      # Extends the given line to fit the whole screen by finding its closed formula! So basically finds a and b so that line = a * x + b. Some odd dudes call it mx + b. Pay those no mind :p

    if v1[0] == v2[0]:
        line_formula = (0, v1[1])                    # it's a horizontal line!

    elif v1[1] == v2[1]:
        line_formula = ("vertical", v1[0])     # it's a vertical line... let's make a flag for it to separate this border case from the rest ":3

    else:
        a = (v2[1] - v1[1]) / (v2[0] - v1[0])
        b = v2[1] - a * v2[0]             # do the math, it checks out :p   v2 and v1 should give the same result here btw              

        line_formula = (a, b)

    return line_formula                   # It's a line! f(x) = a * x + b


def check_colliders_init(v1, v2, v3, vA):   # Looks for the (bool, bool, bool) combination for vA

    line_1 = finds_line_equation(v1, v2)
    line_2 = finds_line_equation(v2, v3)
    line_3 = finds_line_equation(v3, v1)

    lines = [line_1, line_2, line_3]

    vAC = []

    for line in lines:

        if type(line[0]) == str:     # if the line is a vertical one...
            line = (line[1] <  vA[1])
            vAC.append(line)
        else:
            line = (vA[1] <= line[0] * vA[0] + line[1])         # line[0] is a // line [1] is b // vA[0] is x_v // vA[1] is y_v
            vAC.append(line)
            
    # print("lines_combination (vAC) is: ", vAC)
    return vAC

def check_colliders(v1, v2, v3, vAC, vC):   # vAC is the (bool, bool, bool) combination for vA

    rescaled_vC_x = floor(vC[0] * game_width / user_screen_width)
    rescaled_vC_y = floor(vC[1] * game_height / user_screen_height)

    rescaled_vC = (rescaled_vC_x, rescaled_vC_y)

    vCC = (False, False, False) # Initializes vCC
    
    vCC = check_colliders_init(v1, v2, v3, rescaled_vC)
    
    return vAC == vCC   #vCC is the combination calculated based on where the player/cursor is currently located at! :3


if __name__ == "__main__":

    def tests_yellow():
        y_v0 = (1114, 421)
        y_v4 = (1267, 135)
        y_v5 = (1495, 346)

        y_cv2 = (1306, 292)

        vC = (900,200)

        print("Should be True: ", check_colliders(y_v0, y_v4, y_v5, (check_colliders_init(y_v0, y_v4, y_v5, y_cv2)), vC))


    tests_yellow()