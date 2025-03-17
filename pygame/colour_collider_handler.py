from collider_handler import check_colliders_init, check_colliders, set_game_resolution
from geometry import Vertex, Triangle
import pygame

# My game has a 1920 x 1080 resolution world map!
set_game_resolution(1920, 1080)


class Colliders_Colour:
    def __init__(self, vertices, triangles, center_vertices, center_vertices_plane_region):

        self.vertices = vertices
        self.triangles = triangles
        self.center_vertices = center_vertices
        self.center_vertices_plane_region = center_vertices_plane_region

        # self.name = "Yellow"


    def is_user_on_colour(self, mouse_pos_vertex):

        result = False

        cv = -1

        for t in self.triangles:

            cv += 1

            # print("mouse pos: ", mouse_pos)
            # print("Mouse pos as vertex: ", mouse_pos_vertex.x_coordinate(), mouse_pos_vertex.y_coordinate())


            if (check_colliders(t, self.center_vertices_plane_region[cv], mouse_pos_vertex)) == True:
                result = True         # ... then the user is in this region! :D
        
        return result

red = 0
orange = 0
yellow = 0
green = 0
blue = 0
purple = 0

def colours_init():
    
    # red_init()
    # orange_init()
    yellow_init()
    # green_init()
    # blue_init()
    # purple_init()

    return

def yellow_init():

    y_v0 = Vertex(1114, 421)
    y_v1 = Vertex(1116, 335)
    y_v2 = Vertex(1176, 303)
    y_v3 = Vertex(1213, 167)
    y_v4 = Vertex(1267, 135)
    y_v5 = Vertex(1495, 346)

    y_t0 = Triangle(y_v0, y_v1, y_v2)   # The triangle goes like this: t0 = [v0, v1, v2, v0]. Same reasoning behind all other triangles!
    y_t1 = Triangle(y_v2, y_v3, y_v4)
    y_t2 = Triangle(y_v0, y_v4, y_v5)

    y_cv0 = Vertex(1134, 348)
    y_cv1 = Vertex(1227, 179)
    y_cv2 = Vertex(1306, 292)


    # center_vertex_plane_region = (bool, bool, bool)


    # center_vertex_plane_region_0 = check_colliders_init((((y_t0.vertex_1()).x_coordinate()), ((y_t0.vertex_1()).y_coordinate())), (((y_t0.vertex_2()).x_coordinate()), ((y_t0.vertex_2()).y_coordinate())), (((y_t0.vertex_3()).x_coordinate()), ((y_t0.vertex_3()).y_coordinate())), ((y_cv0.x_coordinate()), (y_cv0.y_coordinate())))
    # center_vertex_plane_region_1 = check_colliders_init(y_t1.vertex_1(), y_t1.vertex_2(), y_t1.vertex_3(), y_cv1)
    # center_vertex_plane_region_2 = check_colliders_init(y_t2.vertex_1(), y_t2.vertex_2(), y_t2.vertex_3(), y_cv2)

    center_vertex_plane_region_0 = check_colliders_init(y_t0, y_cv0)
    center_vertex_plane_region_1 = check_colliders_init(y_t1, y_cv1)
    center_vertex_plane_region_2 = check_colliders_init(y_t2, y_cv2)



    yellow_vertices = [y_v0, y_v1, y_v2, y_v3, y_v4, y_v5]
    yellow_triangles = [y_t0, y_t1, y_t2]
    yellow_center_vertices = [y_cv0, y_cv1, y_cv2]
    yellow_center_vertices_plane_region = [center_vertex_plane_region_0, center_vertex_plane_region_1, center_vertex_plane_region_2]

    global yellow
    yellow = Colliders_Colour(yellow_vertices, yellow_triangles, yellow_center_vertices, yellow_center_vertices_plane_region)

    print("Hiii, I'm y_v0. This is my x coordinate: ",
        y_v0.x_coordinate(), "and this is my y coordinate:", y_v0.y_coordinate())

    return