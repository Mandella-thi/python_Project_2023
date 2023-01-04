class Point:
    def __init__(self, x, y):
        self.x = x
        self.y= y
    def  falls_in_rectangle(self, Rectangle):
        if Rectangle.lowLeft.x< self.x <Rectangle.upright.x \
            and Rectangle.lowLeft.y <self.y < Rectangle.upright.y:
            return True
        else:
            return False
    def distance_from_point(self,Point):
        return((self.x -Point.x)**2+(self.y -Point.y)**2)**0.5

class Rectangle:
    def __int__(self,lowleft,upright):
        self.lowleft =lowleft
        self.upright = upright

pointx = Point(6,7)
rectanglex = Rectangle(Point(5,6), Point(7,9))
print(pointx.falls_in_rectangle(rectanglex))

point1 =Point(10, 20)
point2= Point(6,7)
print(point1.x)
#print(point1.falls_in_rectangle((5,6),(7,9)))
print(point1.distance_from_point(point2))