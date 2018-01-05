"""
Estimates pi using Monte Carlo simulation

Algorithm
    - area of virtual dartboard = 4
    - area of unit circle (pi * radius^2) = 1
    - ratio of area of unit circle to area of board = pi/4
    - pi approximation = number of darts that fall within the circle / the total number of darts thrown * 4

Output to monitor:
    - approximation of pi (float)

Output to window:
    - colored dots that simulate unit circle on 2x2 square

Tasks allocated to functions:
    - setUpDartboard() - invokes setworldcoordinates(), drawSquare(), and drawLine()
    - drawSquare() - outlines dartboard
    - drawLine() - draws axes
    - drawCircle() - draws the circle
    - inCircle() - determines if dot is in circle
    - montePi() - simulates algorithm
"""

# List imports here:
import turtle
import math
import random
import time

# List constants here
BOARD_WIDTH = 2
BOARD_RADIUS = 1
DOT_SIZE = 10
RIGHT_ANGLE = 90
PEN_SIZE = 2

# Draws square given turtle, width and top left XY position
def drawSquare(grapher, width, topLeftX, topLeftY):
    grapher.penup();
    grapher.goto(topLeftX, topLeftY)
    grapher.pendown();
    
    for i in range(4):
        grapher.forward(width)
        grapher.right(RIGHT_ANGLE)

# Draws axis-lines given turtle and endpoints
def drawLine(grapher, xStart, yStart, xEnd, yEnd):
    grapher.penup();
    grapher.goto(xStart, yStart)
    grapher.pendown()
    grapher.goto(xEnd, yEnd)

# Draws circle around the origin with given radius
def drawCircle(grapher, radius):
    grapher.penup();
    grapher.goto(0, -radius)
    grapher.pendown()
    grapher.circle(radius, None, 100)

# Sets up 2X2 area with x-axis and y-axis to simulate dartboard
def setUpDartboard(board, grapher):
    # Set up 2X2 area and set pensize
    board.setworldcoordinates(-1.5, -1.5, 1.5, 1.5)
    grapher.pensize(PEN_SIZE)

    # Draw board
    drawSquare(grapher, BOARD_WIDTH, -BOARD_WIDTH / 2, BOARD_WIDTH / 2)

    # Draw x-axis and y-axis
    drawLine(grapher, -BOARD_WIDTH, 0, BOARD_WIDTH, 0)
    drawLine(grapher, 0, BOARD_WIDTH, 0, -BOARD_WIDTH)

    # Draw the circle area
    drawCircle(grapher, BOARD_RADIUS)

# Determines whether or not dart falls inside unit circle with center at (0,0)
def inCircle(dart):
    return dart.distance(0, 0) <= BOARD_RADIUS

# Randomly place a 'dart' on the board
def throwDart(dart):
    # Get random x and y coordinates and then position the dart
    x = random.random() * random.choice([-1, 1])
    y = random.random() * random.choice([-1, 1])

    dart.penup()
    dart.goto(x, y)

    # Draw red dot if in circle, blue dot if not
    if (inCircle(dart)):
        dart.color('red')
        dart.dot(DOT_SIZE)
        return True
    else:
        dart.color('blue')
        dart.dot(DOT_SIZE)
        return False

# Algorithm for Monte Carlo simulation
def montePi(numberDarts, dart):
    inCircleCount = 0

    # Loop for numberDarts
    for d in range(numberDarts):
        if (throwDart(dart)):
            inCircleCount += 1

    ratio = inCircleCount / numberDarts
    return ratio * 4

def main():

    # Create window, turtle, set up window as dartboard
    window = turtle.Screen()

    darty = turtle.Turtle()
    darty.speed(0)
    setUpDartboard(window, darty)

    window.tracer(500)

    numberDarts = int(input("Please input the number of darts to be thrown in the simulation: "))

    # Run simulation and calculate elapsed time
    start_time = time.time()
    print("pi Approximation = " + str(montePi(numberDarts, darty)))
    elapsed_time = time.time() - start_time
    print("Run Time(s):", elapsed_time)

    window.exitonclick()

main()
