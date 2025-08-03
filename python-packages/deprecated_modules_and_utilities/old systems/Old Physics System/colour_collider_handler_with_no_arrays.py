from collider_handler import check_colliders_init, check_colliders, set_game_resolution
from geometry import Vertex, Triangle

import settings

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


# y_v0 = Vertex(1114, 421)
# y_v1 = Vertex(1116, 335)
# y_v2 = Vertex(1175, 302)

y_v0 = o_v10
y_v1 = o_v11
y_v2 = o_v12

# temp3 = y_v2.x_coordinate()
# temp4 = y_v2.y_coordinate()

# y_v2.x_coord = temp3 - jut
# y_v2.y_coord = temp4 - jut

# y_v3 = Vertex(1212, 167)
# y_v4 = Vertex(1266, 134)

y_v3 = o_v9
y_v4 = o_v8

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






g_v0 = o_v13
g_v1 = y_v0
g_v2 = Vertex(1495, 346)
g_v3 = Vertex(1532 + jut, 532)
g_v4 = Vertex(1600 + jut, 561)
g_v5 = Vertex(1585 + jut, 612)
g_v6 = Vertex(1622 + jut, 668)
g_v7 = Vertex(1584, 678 + jut)
g_v8 = Vertex(1478, 735 + jut)
g_v9 = Vertex(1388 - (jut / 2), 731 + jut)
g_v10 = Vertex(1333, 694)
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




# b_v0 = Vertex(783, 634)
# b_v1 = Vertex(899, 615)
# b_v2 = Vertex(897, 532)
# b_v3 = Vertex(1039, 503)
# b_v4 = Vertex(1094, 565)

b_v0 = o_v16
b_v1 = o_v15
b_v2 = o_v14
b_v3 = o_v13
b_v4 = g_v14
b_v5 = g_v13
b_v6 = g_v12
b_v7 = g_v11
b_v8 = g_v10
b_v9 = g_v9
b_v10 = g_v8
b_v11 = g_v7
b_v12 = g_v6
b_v13 = Vertex(1637, 716)
b_v14 = Vertex(1668, 729)
b_v15 = Vertex(1667, 754)
b_v16 = Vertex(1736, 777)
b_v17 = Vertex(1785, 727)
b_v18 = Vertex(1815, 761)
b_v19 = Vertex(1833, 960)
b_v20 = Vertex(1520, 972)
b_v21 = Vertex(1513, 941)
b_v22 = Vertex(1425, 941)
b_v23 = Vertex(1366, 925)
b_v24 = Vertex(1248, 967)
b_v25 = Vertex(1097, 980)
b_v26 = Vertex(969, 975)
b_v27 = Vertex(926, 947)
b_v28 = Vertex(911, 895)
b_v29 = Vertex(878, 835)
b_v30 = Vertex(790, 765)

b_t0 = Triangle(b_v0, b_v1, b_v30)
b_t1 = Triangle(b_v1, b_v5, b_v30)
b_t2 = Triangle(b_v1, b_v4, b_v5)
b_t3 = Triangle(b_v1, b_v2, b_v4)
b_t4 = Triangle(b_v2, b_v3, b_v4)
b_t5 = Triangle(b_v5, b_v29, b_v30)
b_t6 = Triangle(b_v5, b_v6, b_v29)
b_t7 = Triangle(b_v6, b_v7, b_v29)
b_t8 = Triangle(b_v7, b_v28, b_v29)
b_t9 = Triangle(b_v7, b_v24, b_v28)
b_t10 = Triangle(b_v24, b_v25, b_v28)
b_t11 = Triangle(b_v25, b_v27, b_v28)
b_t12 = Triangle(b_v25, b_v26, b_v27)
b_t13 = Triangle(b_v7, b_v8, b_v9)
b_t14 = Triangle(b_v7, b_v9, b_v24)
b_t15 = Triangle(b_v9, b_v23, b_v24)
b_t16 = Triangle(b_v9, b_v22, b_v23)
b_t17 = Triangle(b_v9, b_v10, b_v22)
b_t18 = Triangle(b_v10, b_v21, b_v22)
b_t19 = Triangle(b_v10, b_v15, b_v21)
b_t20 = Triangle(b_v10, b_v13, b_v15)
b_t21 = Triangle(b_v10, b_v11, b_v13)
b_t22 = Triangle(b_v11, b_v12, b_v13)
b_t23 = Triangle(b_v13, b_v14, b_v15)
b_t24 = Triangle(b_v15, b_v16, b_v21)
b_t25 = Triangle(b_v16, b_v20, b_v21)
b_t26 = Triangle(b_v16, b_v17, b_v18)
b_t27 = Triangle(b_v16, b_v18, b_v19)
b_t28 = Triangle(b_v16, b_v19, b_v20)

b_cv0 = Vertex(823, 660)
b_cv1 = Vertex(925, 667)
b_cv2 = Vertex(1042, 600)
b_cv3 = Vertex(953, 575)
b_cv4 = Vertex(1024, 532)
b_cv5 = Vertex(917, 743)
b_cv6 = Vertex(1107, 647)
b_cv7 = Vertex(1137, 705)
b_cv8 = Vertex(949, 838)
b_cv9 = Vertex(1137, 841)
b_cv10 = Vertex(1083, 952)
b_cv11 = Vertex(951, 937)
b_cv12 = Vertex(977, 966)
b_cv13 = Vertex(1328, 713)
b_cv14 = Vertex(1292, 815)
b_cv15 = Vertex(1331, 898)
b_cv16 = Vertex(1394, 901)
b_cv17 = Vertex(1430, 765)
b_cv18 = Vertex(1472, 895)
b_cv19 = Vertex(1565, 787)
b_cv20 = Vertex(1614, 733)
b_cv21 = Vertex(1579, 703)
b_cv22 = Vertex(1617, 684)
b_cv23 = Vertex(1659, 734)
b_cv24 = Vertex(1681, 789)
b_cv25 = Vertex(1541, 936)
b_cv26 = Vertex(1787, 755)
b_cv27 = Vertex(1798, 836)
b_cv28 = Vertex(1708, 895)

center_vertex_plane_region_b0 = check_colliders_init(b_t0, b_cv0)
center_vertex_plane_region_b1 = check_colliders_init(b_t1, b_cv1)
center_vertex_plane_region_b2 = check_colliders_init(b_t2, b_cv2)
center_vertex_plane_region_b3 = check_colliders_init(b_t3, b_cv3)
center_vertex_plane_region_b4 = check_colliders_init(b_t4, b_cv4)
center_vertex_plane_region_b5 = check_colliders_init(b_t5, b_cv5)
center_vertex_plane_region_b6 = check_colliders_init(b_t6, b_cv6)
center_vertex_plane_region_b7 = check_colliders_init(b_t7, b_cv7)
center_vertex_plane_region_b8 = check_colliders_init(b_t8, b_cv8)
center_vertex_plane_region_b9 = check_colliders_init(b_t9, b_cv9)
center_vertex_plane_region_b10 = check_colliders_init(b_t10, b_cv10)
center_vertex_plane_region_b11 = check_colliders_init(b_t11, b_cv11)
center_vertex_plane_region_b12 = check_colliders_init(b_t12, b_cv12)
center_vertex_plane_region_b13 = check_colliders_init(b_t13, b_cv13)
center_vertex_plane_region_b14 = check_colliders_init(b_t14, b_cv14)
center_vertex_plane_region_b15 = check_colliders_init(b_t15, b_cv15)
center_vertex_plane_region_b16 = check_colliders_init(b_t16, b_cv16)
center_vertex_plane_region_b17 = check_colliders_init(b_t17, b_cv17)
center_vertex_plane_region_b18 = check_colliders_init(b_t18, b_cv18)
center_vertex_plane_region_b19 = check_colliders_init(b_t19, b_cv19)
center_vertex_plane_region_b20 = check_colliders_init(b_t20, b_cv20)
center_vertex_plane_region_b21 = check_colliders_init(b_t21, b_cv21)
center_vertex_plane_region_b22 = check_colliders_init(b_t22, b_cv22)
center_vertex_plane_region_b23 = check_colliders_init(b_t23, b_cv23)
center_vertex_plane_region_b24 = check_colliders_init(b_t24, b_cv24)
center_vertex_plane_region_b25 = check_colliders_init(b_t25, b_cv25)
center_vertex_plane_region_b26 = check_colliders_init(b_t26, b_cv26)
center_vertex_plane_region_b27 = check_colliders_init(b_t27, b_cv27)
center_vertex_plane_region_b28 = check_colliders_init(b_t28, b_cv28)



blue_vertices = [b_v0, b_v1, b_v2, b_v3, b_v4, b_v5, b_v6, b_v7, b_v8, b_v9, b_v10, b_v11, b_v12, b_v13, b_v14, b_v15, b_v16, b_v17, b_v18, b_v19, b_v20, b_v21, b_v22, b_v23, b_v24, b_v25, b_v26, b_v27, b_v28, b_v29, b_v30]
blue_triangles = [b_t0, b_t1, b_t2, b_t3, b_t4, b_t5, b_t6, b_t7, b_t8, b_t9, b_t10, b_t11, b_t12, b_t13, b_t14, b_t15, b_t16, b_t17, b_t18, b_t19, b_t20, b_t21, b_t22, b_t23, b_t24, b_t25, b_t26, b_t27, b_t28]
blue_center_vertices = [b_cv0, b_cv1, b_cv2, b_cv3, b_cv4, b_cv5, b_cv6, b_cv7, b_cv8, b_cv9, b_cv10, b_cv11, b_cv12, b_cv13, b_cv14, b_cv15, b_cv16, b_cv17, b_cv18, b_cv19, b_cv20, b_cv21, b_cv22, b_cv23, b_cv24, b_cv25, b_cv26, b_cv27, b_cv28]
blue_center_vertices_plane_region = [center_vertex_plane_region_b0, center_vertex_plane_region_b1, center_vertex_plane_region_b2, center_vertex_plane_region_b3, center_vertex_plane_region_b4, center_vertex_plane_region_b5, center_vertex_plane_region_b6, center_vertex_plane_region_b7, center_vertex_plane_region_b8, center_vertex_plane_region_b9, center_vertex_plane_region_b10, center_vertex_plane_region_b11, center_vertex_plane_region_b12, center_vertex_plane_region_b13, center_vertex_plane_region_b14, center_vertex_plane_region_b15, center_vertex_plane_region_b16, center_vertex_plane_region_b17, center_vertex_plane_region_b18, center_vertex_plane_region_b19, center_vertex_plane_region_b20, center_vertex_plane_region_b21, center_vertex_plane_region_b22, center_vertex_plane_region_b23, center_vertex_plane_region_b24, center_vertex_plane_region_b25, center_vertex_plane_region_b26, center_vertex_plane_region_b27, center_vertex_plane_region_b28]

blue = Colliders_Colour(blue_vertices, blue_triangles, blue_center_vertices, blue_center_vertices_plane_region)







p_v0 = Vertex(177, 645)
# p_v0 = Vertex(176, 645)
p_v1 = Vertex(206, 594)
p_v2 = Vertex(267, 598)
# p_v2 = Vertex(267, 596)
p_v3 = Vertex(344, 539)
p_v4 = o_v0
p_v5 = o_v20
p_v6 = o_v19
p_v7 = o_v18
p_v8 = o_v17
p_v9 = o_v16
p_v10 = b_v30
p_v11 = b_v29
p_v12 = b_v28
p_v13 = b_v27
p_v14 = b_v26
p_v15 = Vertex(400, 1050)
p_v16 = Vertex(226, 1050)

p_t0 = Triangle(p_v0, p_v1, p_v2)
p_t1 = Triangle(p_v0, p_v2, p_v16)
p_t2 = Triangle(p_v2, p_v15, p_v16)
p_t3 = Triangle(p_v2, p_v3, p_v15)
p_t4 = Triangle(p_v3, p_v4, p_v15)
p_t5 = Triangle(p_v4, p_v5, p_v15)
p_t6 = Triangle(p_v5, p_v6, p_v15)
p_t7 = Triangle(p_v6, p_v7, p_v15)
p_t8 = Triangle(p_v7, p_v10, p_v15)
p_t9 = Triangle(p_v10, p_v11, p_v15)
p_t10 = Triangle(p_v11, p_v12, p_v15)
p_t11 = Triangle(p_v12, p_v13, p_v15)
p_t12 = Triangle(p_v13, p_v14, p_v15)
p_t13 = Triangle(p_v8, p_v9, p_v10)
p_t14 = Triangle(p_v7, p_v8, p_v10)

p_cv0 = Vertex(216, 609)
p_cv1 = Vertex(223, 678)
p_cv2 = Vertex(308, 929)
p_cv3 = Vertex(328, 662) #
p_cv4 = Vertex(428, 600) #
p_cv5 = Vertex(526, 599) #
p_cv6 = Vertex(614, 558) #
p_cv7 = Vertex(611, 617) #
p_cv8 = Vertex(646, 770)
p_cv9 = Vertex(778 ,830)
p_cv10 = Vertex(822, 893)
p_cv11 = Vertex(860, 934)
p_cv12 = Vertex(905, 968)
p_cv13 = Vertex(756, 671)
p_cv14 = Vertex(700, 659)

center_vertex_plane_region_p0 = check_colliders_init(p_t0, p_cv0)
center_vertex_plane_region_p1 = check_colliders_init(p_t1, p_cv1)
center_vertex_plane_region_p2 = check_colliders_init(p_t2, p_cv2)
center_vertex_plane_region_p3 = check_colliders_init(p_t3, p_cv3)
center_vertex_plane_region_p4 = check_colliders_init(p_t4, p_cv4)
center_vertex_plane_region_p5 = check_colliders_init(p_t5, p_cv5)
center_vertex_plane_region_p6 = check_colliders_init(p_t6, p_cv6)
center_vertex_plane_region_p7 = check_colliders_init(p_t7, p_cv7)
center_vertex_plane_region_p8 = check_colliders_init(p_t8, p_cv8)
center_vertex_plane_region_p9 = check_colliders_init(p_t9, p_cv9)
center_vertex_plane_region_p10 = check_colliders_init(p_t10, p_cv10)
center_vertex_plane_region_p11 = check_colliders_init(p_t11, p_cv11)
center_vertex_plane_region_p12 = check_colliders_init(p_t12, p_cv12)
center_vertex_plane_region_p13 = check_colliders_init(p_t13, p_cv13)
center_vertex_plane_region_p14 = check_colliders_init(p_t14, p_cv14)




purple_vertices = [p_v0, p_v1, p_v2, p_v3, p_v4, p_v5, p_v6, p_v7, p_v8, p_v9, p_v10, p_v11, p_v12, p_v13, p_v14, p_v15, p_v16]
purple_triangles = [p_t0, p_t1, p_t2, p_t3, p_t4, p_t5, p_t6, p_t7, p_t8, p_t9, p_t10, p_t11, p_t12, p_t13, p_t14]
purple_center_vertices = [p_cv0, p_cv1, p_cv2, p_cv3, p_cv4, p_cv5, p_cv6, p_cv7, p_cv8, p_cv9, p_cv10, p_cv11, p_cv12, p_cv13, p_cv14]
purple_center_vertices_plane_region = [center_vertex_plane_region_p0, center_vertex_plane_region_p1, center_vertex_plane_region_p2, center_vertex_plane_region_p3, center_vertex_plane_region_p4, center_vertex_plane_region_p5, center_vertex_plane_region_p6, center_vertex_plane_region_p7, center_vertex_plane_region_p8, center_vertex_plane_region_p9, center_vertex_plane_region_p10, center_vertex_plane_region_p11, center_vertex_plane_region_p12, center_vertex_plane_region_p13, center_vertex_plane_region_p14]

purple = Colliders_Colour(purple_vertices, purple_triangles, purple_center_vertices, purple_center_vertices_plane_region)





r_v0 = Vertex(333, 25)
r_v1 = o_v1
r_v2 = p_v4
r_v3 = p_v3
r_v4 = p_v2
r_v5 = p_v1
r_v6 = p_v0
r_v7 = Vertex(119, 492)
r_v8 = Vertex(174, 307)

r_t0 = Triangle(r_v0, r_v1, r_v8)
r_t1 = Triangle(r_v1, r_v7, r_v8)
r_t2 = Triangle(r_v1, r_v2, r_v7)
r_t3 = Triangle(r_v2, r_v3, r_v7)
r_t4 = Triangle(r_v3, r_v4, r_v7)
r_t5 = Triangle(r_v4, r_v5, r_v7)
r_t6 = Triangle(r_v5, r_v6, r_v7)

r_cv0 = Vertex(358, 175)
r_cv1 = Vertex(239, 358)
r_cv2 = Vertex(405, 412)
r_cv3 = Vertex(345, 518)
r_cv4 = Vertex(252, 546)
r_cv5 = Vertex(208, 574)
r_cv6 = Vertex(176, 590)

center_vertex_plane_region_r0 = check_colliders_init(r_t0, r_cv0)
center_vertex_plane_region_r1 = check_colliders_init(r_t1, r_cv1)
center_vertex_plane_region_r2 = check_colliders_init(r_t2, r_cv2)
center_vertex_plane_region_r3 = check_colliders_init(r_t3, r_cv3)
center_vertex_plane_region_r4 = check_colliders_init(r_t4, r_cv4)
center_vertex_plane_region_r5 = check_colliders_init(r_t5, r_cv5)
center_vertex_plane_region_r6 = check_colliders_init(r_t6, r_cv6)


red_vertices = [r_v0, r_v1, r_v2, r_v3, r_v4, r_v5, r_v6, r_v7, r_v8]
red_triangles = [r_t0, r_t1, r_t2, r_t3, r_t4, r_t5, r_t6]
red_center_vertices = [r_cv0, r_cv1, r_cv2, r_cv3, r_cv4, r_cv5, r_cv6]
red_center_vertices_plane_region = [center_vertex_plane_region_r0, center_vertex_plane_region_r1, center_vertex_plane_region_r2, center_vertex_plane_region_r3, center_vertex_plane_region_r4, center_vertex_plane_region_r5, center_vertex_plane_region_r6]

red = Colliders_Colour(red_vertices, red_triangles, red_center_vertices, red_center_vertices_plane_region)



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
    def test_4(vertex):
        vertex_to_test = Vertex(vertex[0], vertex[1])
        print(purple.is_user_on_colour(vertex_to_test))
        return


    
    test_4((50, 1300))      #   <--- Should be FALSE
    test_4((100, 100))          #   <--- Should be FALSE
    test_4((1000, 100))          #   <--- Should be FALSE

    print("\n")

    test_4((814, 100))          #   <--- Should be FALSE        ---     Combination: [False, False, False]
    test_4((815, 100))          #   <--- Should be FALSE        ---     Combination: [False, True, True]


    test_4(((947, 711)))    #   <--- Should be FALSE.   Problematic triangle: p_cv2
    


    """
    import time

    start_time = time.time()
    test_1((1000, 300))
    time.sleep(1)
    print("--- %s seconds ---" % (time.time() - start_time))
    """