import math
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)

    def __str__(self):
        return (self.x, self.y).__str__()

class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        return Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)

    def length(self):
        self.p1.distance(p2)

class Circle(object):-

    def __init__(self, centre, radius):
        self.radius = float(radius)
        self.centre = centre

    def overlaps(self, c2):
        return self.radius + c2.radius > self.centre.distance(c2.centre)
