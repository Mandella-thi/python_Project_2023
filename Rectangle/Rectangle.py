from points import Point


class Rectangle:
    def __int__(self,lowleft,upright):
        self.lowleft =lowleft
        self.upright = upright

pointx = Point(6,7)
rectanglex =Rectangle(Point(5,6), Point(7,9))
print(pointx.falls_in_rectangle(rectanglex))
#teste