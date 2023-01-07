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
        canvas.forward(self.point2.x -self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y -self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x -self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

class GuiPoint(Point):
    def draw (self, canvas, size= 5,color ='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size,color)



#pointx = Point(6,7)
#rectanglex = GuiRectangle(Point(5,6), Point(7,9))
#print("****************************************")
#print(pointx.falls_in_rectangle(rectanglex))
#print("*******************************************")

#point1 =Point(10, 20)
#point2= Point(6,7)
#print(point1.x)
#print(point1.falls_in_rectangle((5,6),(7,9)))
#print(point1.distance_from_point(point2))
rectangle1 =GuiRectangle(Point(randint(0,400),randint(0,400)),
                     Point(randint(410,419),randint(410,419)))
print("Rectangle Coordinates: ", rectangle1.point2.x,
      ",", rectangle1.point2.y, "and",
      rectangle1.point1.x,",", rectangle1.point1.y)
user_point = GuiPoint(float(input("Guess X: ")),
                   float(input("Gues Y: ")))

print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle1),
      "\nThe area of the rectangle is: ", rectangle1.area())
myturtle = turtle.Turtle()
rectangle1.draw(canvas= myturtle)
user_point.draw(canvas= myturtle)
turtle.done()
