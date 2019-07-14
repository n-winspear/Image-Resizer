#Point Class

from math import sqrt

class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def shift(self, x, y):
        self.x += x
        self.y += y

    def distance(a, b):
    	return sqrt((a.x-b.x)**2+(a.y-b.y)**2)