import turtle
import math

def drawPolygon(t, side_length, num_sides):
    """
    Make turtle (t) draw a polygon with side length (side_length) and number of sides (num_sides).
    args: 
        t: turtle
        side_length: side length
        num_sides: number of sides
    """
    angle = 360 / num_sides

    for i in range(num_sides):
        t.forward(side_length)
        t.left(angle)

def drawSquare(t, side_length):
    """
    Make turtle (t) draw a square with side length (side_length).
    args: 
        t: turtle
        side_length: side length
    """
    drawPolygon(t, side_length, 4)
    

def drawTriangle(t, side_length):
    """
    Make turtle (t) draw a triangle with side length (side_length).
    args: 
        t: turtle
        side_length: side length
    """
    drawPolygon(t, side_length, 3)

def drawHexagon(t, side_length):
    """
    Make turtle (t) draw a hexagon with side length (side_length).
    args: 
        t: turtle
        side_length: side length
    """
    drawPolygon(t, side_length, 6)

def drawCircle(t, radius):
    """
    Make turtle (t) draw a circle with radius (radius).
    args: 
        t: turtle
        radius: radius
    """

    t.goto(0, -1 * radius)

    circumference = 2 * math.pi * radius
    side_length = circumference / 360

    drawPolygon(t, side_length, 360)

def drawFilledCircle(t, radius, color):
    """
    Make turtle (t) draw a circle with radius (radius) and color (color).
    args: 
        t: turtle
        radius: radius
        color: color
    """
    
    t.goto(0, -1 * radius)

    t.fillcolor(color)
    t.begin_fill()
    drawCircle(t, radius)
    t.end_fill()

def main():

    window = turtle.Screen()

    franklin = turtle.Turtle()
    franklin.color('blue')
    franklin.shape('turtle')

    drawSquare(franklin, 50)
    drawTriangle(franklin, 100)
    drawHexagon(franklin, 50)
    drawPolygon(franklin, 50, 10)
    drawCircle(franklin, 50)
    drawFilledCircle(franklin, 25, 'red')

    window.exitonclick()

main()
