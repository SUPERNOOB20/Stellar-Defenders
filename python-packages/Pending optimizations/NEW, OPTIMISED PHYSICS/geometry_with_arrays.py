from array import array

class Vertex:
    def __init__(self):
        self.vertex = array("h", [0, 0])

    def get_x_coordinate(self):
        return self[0]
    
    def get_y_coordinate(self):
        return self[1]
    
    def set_coordinates(self, x_coordinate, y_coordinate):
        self[0] = x_coordinate
        self[1] = y_coordinate

class Triangle:
    def __init__(self):
        self.triangle = array(Vertex[0, 0], Vertex[0, 0], Vertex[0, 0])

    def get_vertex_1(self):
        return self[0]
    
    def get_vertex_2(self):
        return self[1]
    
    def get_vertex_3(self):
        return self[2]
    
    def set_vertices(self, vertex_1, vertex_2, vertex_3):
        self[0] = vertex_1
        self[1] = vertex_2
        self[2] = vertex_3

class Line:
    def __init__(self):
        self.line = array("d", [0.0, 0.0])

    def get_slope(self):
        return self[0]
    
    def get_ordinates(self):
        return self[1]
    
    def set_line(self, slope, ordinates):
        self[0] = slope
        self[1] = ordinates