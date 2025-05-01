from collider_handler import check_colliders_init, check_colliders, set_game_resolution
from geometry import Vertex, Triangle

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

            if (check_colliders(t, self.center_vertices_plane_region[cv], mouse_pos_vertex)) == True:       # (Triangle, [bool, bool, bool], Vertex)
                # print("The problematic orange triangle is:", "o_t" + str(cv))
                result = True      # ... then the user is in this region! :D
                break
            
        return result

# red = 0
# orange = 0
# yellow = 0
# green = 0
# blue = 0
# purple = 0

o_v0 = Vertex(502, 501)
o_v1 = Vertex(549, 230)
o_v2 = Vertex(692, 208)
o_v3 = Vertex(705, 168)
o_v4 = Vertex(744, 147)
o_v5 = Vertex(741, 174)
o_v6 = Vertex(762, 227)
o_v7 = Vertex(1048, 153)
o_v8 = Vertex(1266, 134)
o_v9 = Vertex(1212, 167)
o_v10 = Vertex(1175, 302)
# o_v11 = Vertex(1115, 335)                   # !!!
# o_v12 = Vertex(1115, 421)                   # !!!
o_v11 = Vertex(1116, 335)
o_v12 = Vertex(1114, 421)
o_v13 = Vertex(1039, 504)
o_v14 = Vertex(897, 533)
o_v15 = Vertex(899, 615)
o_v16 = Vertex(783, 634)
o_v17 = Vertex(708, 646)
o_v18 = Vertex(629, 610)
o_v19 = Vertex(630, 551)
o_v20 = Vertex(611, 525)


o_t0 = Triangle(o_v0, o_v1, o_v2)
o_t1 = Triangle(o_v3, o_v4, o_v5)
o_t2 = Triangle(o_v2, o_v3, o_v5)
o_t3 = Triangle(o_v2, o_v5, o_v6)
o_t4 = Triangle(o_v0, o_v2, o_v20)
o_t5 = Triangle(o_v2, o_v6, o_v20)
o_t6 = Triangle(o_v6, o_v19, o_v20)
o_t7 = Triangle(o_v6, o_v18, o_v19)
o_t8 = Triangle(o_v6, o_v16, o_v18)
o_t9 = Triangle(o_v6, o_v14, o_v16)
o_t10 = Triangle(o_v6, o_v13, o_v14)
o_t11 = Triangle(o_v6, o_v12, o_v13)
o_t12 = Triangle(o_v6, o_v11, o_v12)
o_t13 = Triangle(o_v6, o_v7, o_v11)
o_t14 = Triangle(o_v7, o_v10, o_v11)
o_t15 = Triangle(o_v7, o_v9, o_v10)
o_t16 = Triangle(o_v7, o_v8, o_v9)
o_t17 = Triangle(o_v16, o_v17, o_v18)
o_t18 = Triangle(o_v14, o_v15, o_v16)




o_cv0 = Vertex(603, 282)
o_cv1 = Vertex(733, 163)
o_cv2 = Vertex(712, 182)
o_cv3 = Vertex(728, 202)
o_cv4 = Vertex(595, 423)
o_cv5 = Vertex(701, 270)
o_cv6 = Vertex(634, 507)
o_cv7 = Vertex(641, 553)
o_cv8 = Vertex(727, 441)
o_cv9 = Vertex(817, 447)
o_cv10 = Vertex(920, 450)
o_cv11 = Vertex(1005, 406)
o_cv12 = Vertex(1043, 347)
o_cv13 = Vertex(1026, 246)
o_cv14 = Vertex(1122, 275)
o_cv15 = Vertex(1154, 214)
o_cv16 = Vertex(1206, 152)
o_cv17 = Vertex(709, 633)
o_cv18 = Vertex(871, 590)




#center_vertex_plane_region_xY return the [bool, bool, bool] for each collider (this should be calculated before the game starts!!!)
center_vertex_plane_region_o0: list[bool] = check_colliders_init(o_t0, o_cv0)
center_vertex_plane_region_o1 = check_colliders_init(o_t1, o_cv1)
center_vertex_plane_region_o2 = check_colliders_init(o_t2, o_cv2)
center_vertex_plane_region_o3 = check_colliders_init(o_t3, o_cv3)
center_vertex_plane_region_o4 = check_colliders_init(o_t4, o_cv4)
center_vertex_plane_region_o5 = check_colliders_init(o_t5, o_cv5)
center_vertex_plane_region_o6 = check_colliders_init(o_t6, o_cv6)
center_vertex_plane_region_o7 = check_colliders_init(o_t7, o_cv7)
center_vertex_plane_region_o8 = check_colliders_init(o_t8, o_cv8)
center_vertex_plane_region_o9 = check_colliders_init(o_t9, o_cv9)
center_vertex_plane_region_o10 = check_colliders_init(o_t10, o_cv10)
center_vertex_plane_region_o11 = check_colliders_init(o_t11, o_cv11)
center_vertex_plane_region_o12 = check_colliders_init(o_t12, o_cv12)
center_vertex_plane_region_o13 = check_colliders_init(o_t13, o_cv13)
center_vertex_plane_region_o14 = check_colliders_init(o_t14, o_cv14)
center_vertex_plane_region_o15 = check_colliders_init(o_t15, o_cv15)
center_vertex_plane_region_o16 = check_colliders_init(o_t16, o_cv16)
center_vertex_plane_region_o17 = check_colliders_init(o_t17, o_cv17)
center_vertex_plane_region_o18 = check_colliders_init(o_t18, o_cv18)



orange_vertices = [o_v0, o_v1, o_v2, o_v3, o_v4, o_v5, o_v6, o_v7, o_v8, o_v9, o_v10, o_v11, o_v12, o_v13, o_v14, o_v15, o_v16, o_v17, o_v18, o_v19, o_v20]
orange_triangles = [o_t0, o_t1, o_t2, o_t3, o_t4, o_t5, o_t6, o_t7, o_t8, o_t9, o_t10, o_t11, o_t12, o_t13, o_t14, o_t15, o_t16, o_t17, o_t18]
orange_center_vertices = [o_cv0, o_cv1, o_cv2, o_cv3, o_cv4, o_cv5, o_cv6, o_cv7, o_cv8, o_cv9, o_cv10, o_cv11, o_cv12, o_cv13, o_cv14, o_cv15, o_cv16, o_cv17, o_cv18]
orange_center_vertices_plane_region = [center_vertex_plane_region_o0, center_vertex_plane_region_o1, center_vertex_plane_region_o2, center_vertex_plane_region_o3, center_vertex_plane_region_o4, center_vertex_plane_region_o5, center_vertex_plane_region_o6, center_vertex_plane_region_o7, center_vertex_plane_region_o8, center_vertex_plane_region_o9, center_vertex_plane_region_o10, center_vertex_plane_region_o11, center_vertex_plane_region_o12, center_vertex_plane_region_o13, center_vertex_plane_region_o14, center_vertex_plane_region_o15, center_vertex_plane_region_o16, center_vertex_plane_region_o17, center_vertex_plane_region_o18]

orange = Colliders_Colour(orange_vertices, orange_triangles, orange_center_vertices, orange_center_vertices_plane_region)




jut = 4     # Juts out the specified amount of pixels to attempt to avoid edge misalignments (remember that 3-hour pancake video? Well, that's where I got inspired from to implement this workaround :P).
            # Side note: If this causes the player to "appearently" be on two regions at the same time, that's no biggie - my code is implemented in a way that avoids this :)
            # Side note #2: Try not to jut a region into other regions, as this may hindrance user experience (i.e trying to point to a region but being directed towards a different one...)


y_v0 = Vertex(1114, 421)
y_v1 = Vertex(1116, 335)
y_v2 = Vertex(1175, 302)

temp3 = y_v2.x_coordinate()
temp4 = y_v2.y_coordinate()

y_v2.x_coord = temp3 - jut
y_v2.y_coord = temp4 - jut

y_v3 = Vertex(1212, 167)
y_v4 = Vertex(1266, 134)
y_v5 = Vertex(1495 + 3 * jut, 346)

y_v6 = Vertex(1114 - 5 * jut, 421)
y_v7 = Vertex(1266, 134 - 5 * jut)


y_t0 = Triangle(y_v0, y_v1, y_v2)   # The triangle goes like this: t0 = [v0, v1, v2, v0]. Same reasoning behind all other triangles!
y_t1 = Triangle(y_v2, y_v3, y_v4)
y_t2 = Triangle(y_v0, y_v4, y_v5)
y_t3 = Triangle(y_v5, y_v6, y_v7)

y_cv0 = Vertex(1134, 348)
y_cv1 = Vertex(1227, 179)
y_cv2 = Vertex(1306, 292)
y_cv3 = Vertex(1306, 292)

center_vertex_plane_region_y0 = check_colliders_init(y_t0, y_cv0)
center_vertex_plane_region_y1 = check_colliders_init(y_t1, y_cv1)
center_vertex_plane_region_y2 = check_colliders_init(y_t2, y_cv2)
center_vertex_plane_region_y3 = check_colliders_init(y_t3, y_cv3)


yellow_vertices = [y_v0, y_v1, y_v2, y_v3, y_v4, y_v5, y_v6, y_v7]
yellow_triangles = [y_t0, y_t1, y_t2, y_t3]
yellow_center_vertices = [y_cv0, y_cv1, y_cv2, y_cv3]
yellow_center_vertices_plane_region = [center_vertex_plane_region_y0, center_vertex_plane_region_y1, center_vertex_plane_region_y2, center_vertex_plane_region_y3]

yellow = Colliders_Colour(yellow_vertices, yellow_triangles, yellow_center_vertices, yellow_center_vertices_plane_region)






g_v0 = Vertex(1039, 504)
g_v1 = Vertex(1114, 421)
g_v2 = Vertex(1495, 346)
g_v3 = Vertex(1532 + jut, 532)
g_v4 = Vertex(1600 + jut, 561)
g_v5 = Vertex(1585 + jut, 612)
g_v6 = Vertex(1622 + jut, 668)
g_v7 = Vertex(1584, 678 + jut)
g_v8 = Vertex(1478, 735 + jut)
g_v9 = Vertex(1388 - (jut / 2), 731 + jut)
g_v10 = Vertex(1333 - (jut / 2), 694 + jut)
g_v11 = Vertex(1240, 714)
g_v12 = Vertex(1157 - jut, 637 + jut)
g_v13 = Vertex(1095, 620)
g_v14 = Vertex(1093 - jut, 566)

g_t0 = Triangle(g_v0, g_v1, g_v14)
g_t1 = Triangle(g_v1, g_v2, g_v3)
g_t2 = Triangle(g_v1, g_v3, g_v14)
g_t3 = Triangle(g_v14, g_v3, g_v5)
g_t4 = Triangle(g_v3, g_v4, g_v5)
g_t5 = Triangle(g_v14, g_v5, g_v10)
g_t6 = Triangle(g_v5, g_v8, g_v10)
g_t7 = Triangle(g_v5, g_v7, g_v8)
g_t8 = Triangle(g_v5, g_v6, g_v7)
g_t9 = Triangle(g_v8, g_v9, g_v10)
g_t10 = Triangle(g_v10, g_v11, g_v12)
g_t11 = Triangle(g_v10, g_v12, g_v14)
g_t12 = Triangle(g_v12, g_v13, g_v14)

g_cv0 = Vertex(1078, 500)
g_cv1 = Vertex(1384, 434)
g_cv2 = Vertex(1250, 514)
g_cv3 = Vertex(1444, 571)
g_cv4 = Vertex(1577, 571)
g_cv5 = Vertex(1342, 637)
g_cv6 = Vertex(1473, 688)
g_cv7 = Vertex(1558, 668)
g_cv8 = Vertex(1600, 656)
g_cv9 = Vertex(1391, 727)
g_cv10 = Vertex(1245, 689)
g_cv11 = Vertex(1173, 628)
g_cv12 = Vertex(1112, 609)



center_vertex_plane_region_g0 = check_colliders_init(g_t0, g_cv0)
center_vertex_plane_region_g1 = check_colliders_init(g_t1, g_cv1)
center_vertex_plane_region_g2 = check_colliders_init(g_t2, g_cv2)
center_vertex_plane_region_g3 = check_colliders_init(g_t3, g_cv3)
center_vertex_plane_region_g4 = check_colliders_init(g_t4, g_cv4)
center_vertex_plane_region_g5 = check_colliders_init(g_t5, g_cv5)
center_vertex_plane_region_g6 = check_colliders_init(g_t6, g_cv6)
center_vertex_plane_region_g7 = check_colliders_init(g_t7, g_cv7)
center_vertex_plane_region_g8 = check_colliders_init(g_t8, g_cv8)
center_vertex_plane_region_g9 = check_colliders_init(g_t9, g_cv9)
center_vertex_plane_region_g10 = check_colliders_init(g_t10, g_cv10)
center_vertex_plane_region_g11 = check_colliders_init(g_t11, g_cv11)
center_vertex_plane_region_g12 = check_colliders_init(g_t12, g_cv12)



green_vertices = [g_v0, g_v1, g_v2, g_v3, g_v4, g_v5, g_v6, g_v7, g_v8, g_v9, g_v10, g_v11, g_v12, g_v13, g_v14]
green_triangles = [g_t0, g_t1, g_t2, g_t3, g_t4, g_t5, g_t6, g_t7, g_t8, g_t9, g_t10, g_t11, g_t12]
green_center_vertices = [g_cv0, g_cv1, g_cv2, g_cv3, g_cv4, g_cv5, g_cv6, g_cv7, g_cv8, g_cv9, g_cv10, g_cv11, g_cv12]
green_center_vertices_plane_region = [center_vertex_plane_region_g0, center_vertex_plane_region_g1, center_vertex_plane_region_g2, center_vertex_plane_region_g3, center_vertex_plane_region_g4, center_vertex_plane_region_g5, center_vertex_plane_region_g6, center_vertex_plane_region_g7, center_vertex_plane_region_g8, center_vertex_plane_region_g9, center_vertex_plane_region_g10, center_vertex_plane_region_g11, center_vertex_plane_region_g12]

green = Colliders_Colour(green_vertices, green_triangles, green_center_vertices, green_center_vertices_plane_region)



if __name__ == "__main__":

    def test_0():
        print("ok ok!!! :3")
        print('test case for false positive Orange underway, mistress! ":S')
        print("Is (56, 510) inside of the Orange region??? ---> ")
        
        pito = Vertex(56, 510)
        pito_rescaled = Vertex(78, 717)
        print("center_vertex_plane_region_o5:", center_vertex_plane_region_o5)

        # print(check_colliders(o_t5, o_cv5, pito))       # This should NOT BE VALID TYPING.
        print(check_colliders(o_t5, center_vertex_plane_region_o5, pito))       # This should print False

        print("/n /n /n /n /n")
        print(check_colliders_init(o_t5, o_cv5))
        print(check_colliders_init(o_t5, pito_rescaled))
        print("ignore (lmao) --->", check_colliders_init(o_t5, pito))
        print("is user on colour Orange? (this should be [idkkk]) --->", orange.is_user_on_colour(o_cv5))


        o_cv5_reescaled_inv = Vertex(498, 191)
        print("is user on colour Orange? (this should be TRUE) --->", orange.is_user_on_colour(o_cv5_reescaled_inv))
        return

    def test_1(vertex):
        vertex_to_test = Vertex(vertex[0], vertex[1])
        print(orange.is_user_on_colour(vertex_to_test))
        return
    
    def test_2(vertex):
        vertex_to_test = Vertex(vertex[0], vertex[1])
        print(green.is_user_on_colour(vertex_to_test))
        return
    def test_3(vertex):
        vertex_to_test = Vertex(vertex[0], vertex[1])
        print(yellow.is_user_on_colour(vertex_to_test))
        return

    # test_1((1231, 455))
    # test_2((1350, 300))
    # test_3((1153,363))           # (821,242)
    test_3((821,242))