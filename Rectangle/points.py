from random import randint
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
    def __init__(self,lowLeft,upright):
        self.lowLeft =lowLeft
        self.upright = upright
    def area(self,):
        return (self.upright.x -self.lowLeft.x)* \
            (self.upright.y -self.lowLeft.y)

pointx = Point(6,7)
rectanglex = Rectangle(Point(5,6), Point(7,9))
print("****************************************")
print(pointx.falls_in_rectangle(rectanglex))
print("*******************************************")

point1 =Point(10, 20)
point2= Point(6,7)
print(point1.x)
#print(point1.falls_in_rectangle((5,6),(7,9)))
print(point1.distance_from_point(point2))
rectangle1 =Rectangle(Point(randint(0,9),randint(0,9)),
                     Point(randint(10,19),randint(10,19)))
print("Rectangle Coordinates: ", rectangle1.lowLeft.x,
      ",", rectangle1.lowLeft.y, "and",
      rectangle1.upright.x,",", rectangle1.upright.y)
user_point = Point(float(input("Guess X: ")),
                   float(input("Gues Y: ")))

print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle1), "\nThe area of the rectangle is: ", rectangle1.area())