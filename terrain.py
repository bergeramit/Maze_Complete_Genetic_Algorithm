from vectors_util import Vector

class Terrain:
    def __init__(self, x, y, height, width, color):
        self.position = Vector(x, y)
        self.height = height
        self.width = width
        self.color = color
