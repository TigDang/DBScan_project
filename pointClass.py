import math


class Point:
    width = 1
    height = 1

    def __init__(self, x, y, r, g, b):
        self.label = 'Undefined'
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        if Point.width < self.x:
            Point.width = self.x
        if Point.height < self.y:
            Point.height = self.y

    def __iter__(self):
        self.x = 0
        self.y = 0
        return self

    def __next__(self):
        if self.x != self.width:
            self.x +=1
            return self
        else:
            if self.y != self.height:
                self.x = 0
                self.y +=1
                return self
            else:
                raise StopIteration

    def setLabel(self, label):
        self.label = label

    def getMetric(a, b):
        dx = (a.x - b.x)
        dy = (a.y - b.y)
        dr = (int(a.r) - int(b.r))
        dg = (int(a.g) - int(b.g))
        db = (int(a.b) - int(b.b))
        return math.sqrt(dx ** 2 + dy ** 2 + dr ** 2 + dg ** 2 + db ** 2)
