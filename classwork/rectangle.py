import turtle

def drawRectangle(d, width, height):
    for i in range(2):
        d.forward(width)
        d.left(90)
        d.forward(height)
        d.left(90)

def main():

    width = int(input('Please Enter a Width: '))
    height = int(input('Please Enter a Height: '))

    window = turtle.Screen()

    d = turtle.Turtle()
    drawRectangle(d, width, height)

    window.exitonclick()

main()
