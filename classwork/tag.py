import turtle
import random

def main():

    window = turtle.Screen()
    window.bgcolor('green')

    turtle1 = turtle.Turtle()
    turtle1.shape('turtle')
    turtle1.color('red')
    turtle1.penup()
    turtle1.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle1.speed(5)

    turtle2 = turtle.Turtle()
    turtle2.shape('turtle')
    turtle2.color('blue')
    turtle2.penup()
    turtle2.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle2.speed(1)

    while not turtle1.distance(turtle2.xcor(), turtle2.ycor()) < 25:
        turtle2.goto(random.randint(-100, 100), random.randint(-100, 100))
        window.onclick(turtle1.goto)

    print('You Win!')

main()
