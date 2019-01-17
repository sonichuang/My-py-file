import math as m
class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def getlen(self):
        len = m.sqrt((self.x2 - self.x1)**2 + (self.y2 -  self.y1)**2)
        return len

p = Point(0, 0, 2, 2)
l = p.getlen()
print(l)
        
