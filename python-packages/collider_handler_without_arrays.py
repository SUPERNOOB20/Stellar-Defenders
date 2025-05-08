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

from geometry import Triangle, Vertex, Line

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

set_game_resolution(1920, 1080)
# print("game resolution is OK:", str(game_width) ++ "x" ++ str(game_height))

def finds_line_equation(vertex_1: Vertex, vertex_2: Vertex):      # Extends the given line to fit the whole screen by finding its closed formula! So basically finds a and b so that line = a * x + b. Some odd dudes call it mx + b. Pay those no mind :p

    if vertex_1.y_coordinate() == vertex_2.y_coordinate():
        line_formula = Line(0, vertex_1.y_coordinate())                    # it's a horizontal line!

    elif vertex_1.x_coordinate() == vertex_2.x_coordinate():
        line_formula = Line("vertical", vertex_1.x_coordinate())     # it's a vertical line... let's make a flag for it to separate this border case from the rest ":3
        # in this case line_formula isn't the closed formula, so instead of line(a, b) here we have line("vertical", x_0), but oh well... ":3


    else:
        a = (vertex_2.y_coordinate() - vertex_1.y_coordinate()) / (vertex_2.x_coordinate() - vertex_1.x_coordinate())
        b = vertex_2.y_coordinate() - a * vertex_2.x_coordinate()             # do the math, it checks out :p  ///  vertex_2 and vertex_1 should give the same result here btw              

        line_formula = Line(a, b)

    return line_formula                   # It's a line! f(x) = a * x + b


def check_colliders_init(triangle: Triangle, vertex_A: Vertex):   # Looks for the (bool, bool, bool) combination for vA

    line_1 = finds_line_equation(triangle.vertex_1(), triangle.vertex_2())
    line_2 = finds_line_equation(triangle.vertex_2(), triangle.vertex_3())
    line_3 = finds_line_equation(triangle.vertex_3(), triangle.vertex_1())

    lines = [line_1, line_2, line_3]

    vertex_AC = []

    for line in lines:

        if type(line.slope()) == str:     # if the line is a vertical one...
            line = (line.ordinates() < vertex_A.x_coordinate())    # here, line.ordinates() is just the x value of the vertical line (sorry for notation abuse, coding is hard... e.e) 
            vertex_AC.append(line)
        else:
            line = (vertex_A.y_coordinate() <= line.slope() * vertex_A.x_coordinate() + line.ordinates())         # line[0] is a // line [1] is b // vA[0] is x_v // vA[1] is y_v
            vertex_AC.append(line)
            
    # print("lines_combination (vertex_AC) is: ", vertex_AC)
    return vertex_AC

def check_colliders(triangle: Triangle, vertex_AC: list[bool], vertex_C: Vertex):   # vertex_AC is the [bool, bool, bool] combination for vertex_A

    rescaled_vertex_C_x_coordinate = floor(vertex_C.x_coordinate() * game_width / user_screen_width)
    rescaled_vertex_C_y_coordinate = floor(vertex_C.y_coordinate() * game_height / user_screen_height)

    rescaled_vertex_C = Vertex(rescaled_vertex_C_x_coordinate, rescaled_vertex_C_y_coordinate)  # We have to rescale user input!!! Because their screen might not be the same as the game resolution!":3

    # print("game_width =", game_width)
    # print("game_height =", game_height)

    vertex_CC = [False, False, False] # Initializes vertex_CC
    
    vertex_CC = check_colliders_init(triangle, rescaled_vertex_C)


    return vertex_AC == vertex_CC   # vertex_CC is the combination calculated based on where the player/cursor is currently located at! :3


"""
def check_against_initialized_colliders(triangle: Triangle, bool_list: list[bool], vertex):
    check_for_current_triangle = check_colliders(triangle, Vertex)
    return
"""
    

"""
if __name__ == "__main__":

    def tests_yellow():
        y_v0 = (1114, 421)
        y_v4 = (1267, 135)
        y_v5 = (1495, 346)

        y_cv2 = (1306, 292)

        vC = (900,200)

        print("Should be True: ", check_colliders(y_v0, y_v4, y_v5, (check_colliders_init(y_v0, y_v4, y_v5, y_cv2)), vC))


    tests_yellow()
"""
