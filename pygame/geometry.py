class Vertex:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def x_coordinate(self):
        return self.x_coord
    
    def y_coordinate(self):
        return self.y_coord


class Triangle:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def vertex_1(self):
        return self.v1
    
    def vertex_2(self):
        return self.v2
    
    def vertex_3(self):
        return self.v3


class Line:
    def __init__(self, slope, ordinates):
        self.slope_parameter = slope
        self.ordinates_parameter = ordinates

    def slope(self):
        return self.slope_parameter
    
    def ordinates(self):
        return self.ordinates_parameter