from random import randint
import turtle
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y= y
    def  falls_in_rectangle(self, Rectangle):
        if Rectangle.point2.x< self.x <Rectangle.point1.x \
            and Rectangle.point2.y <self.y < Rectangle.point1.y:
            return True
        else:
            return False
    def distance_from_point(self,Point):
        return((self.x -Point.x)**2+(self.y -Point.y)**2)**0.5

class Rectangle:
    def __init__(self,point2,point1):
        self.point2 =point2
        self.point1 = point1
    def area(self,):
        return (self.point1.x - self.point2.x)* \
            (self.point1.y - self.point2.y)

class GuiRectangle(Rectangle): #herança em Python
    def draw(self,canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(100)
        canvas.left(90)
        canvas.forward(110)
        canvas.left(90)
        canvas.forward(100)
        canvas.left(90)
        canvas.forward(110)
        turtle.done()

gui_rectangle =GuiRectangle(Point(randint(0,400),randint(0,400)),
                Point(randint(0,400),randint(0,400)))
myturtle =turtle.Turtle()
gui_rectangle.draw(canvas= myturtle)
print(gui_rectangle.area())

#pointx = Point(6,7)
#rectanglex = Rectangle(Point(5,6), Point(7,9))
#print("****************************************")
#print(pointx.falls_in_rectangle(rectanglex))
#print("*******************************************")

#point1 =Point(10, 20)
#point2= Point(6,7)
#print(point1.x)
#print(point1.falls_in_rectangle((5,6),(7,9)))
#print(point1.distance_from_point(point2))
#rectangle1 =Rectangle(Point(randint(0,400),randint(0,400)),
 #                    Point(randint(410,419),randint(410,419)))
#print("Rectangle Coordinates: ", rectangle1.lowLeft.x,
 #     ",", rectangle1.lowLeft.y, "and",
  #    rectangle1.upright.x,",", rectangle1.upright.y)
#user_point = Point(float(input("Guess X: ")),
#                   float(input("Gues Y: ")))

#print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle1), "\nThe area of the rectangle is: ", rectangle1.area())