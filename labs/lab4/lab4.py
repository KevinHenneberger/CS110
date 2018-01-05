import turtle
import math

# global screen constants 
X_RANGE_LOW = -math.pi * 2
X_RANGE_UPP = math.pi * 2
Y_RANGE_LOW = -1
Y_RANGE_UPP = 1

def mySine(x):
    """
    description:
        calculate sin(x) using the Maclaurin Series for sin(x) to approximate the value
    args: 
        x: angle
    """

    val = 0

    for n in range(25):
        val += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1) # (-1)^n x^(2n + 1) / (2n + 1)!

    return val

def myCosine(x):
    """
    description:
        calculate cos(x) using the Maclaurin Series for cos(x) to approximate the value
    args: 
        x: angle
    """

    val = 0

    for n in range(25):
        val += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n) # (-1)^n x^(2n) / (2n)!

    return val

def myRadians(x):
    """
    description:
        convert angle (x) from degrees to radians
    args: 
        x: angle
    """

    return x * math.pi / 180

def setUpWindow(w):
    """
    description:
        convert the standard screen coordinates to the desired coordinates and set background color
    args: 
        w: window object
    """

    w.setworldcoordinates(X_RANGE_LOW, Y_RANGE_LOW, X_RANGE_UPP, Y_RANGE_UPP)
    w.bgcolor('gray')

def setUpTurtle(t):
    """
    description:
        use turtle to draw the x-axis and y-axis and set turtle to the starting position
    args: 
        t: turtle object
    """

    # draw x-axis
    t.penup();
    t.goto(X_RANGE_LOW, 0)
    t.pendown()
    t.forward(X_RANGE_UPP * 2);

    # draw y-axis
    t.penup();
    t.goto(0, Y_RANGE_UPP)
    t.pendown()
    t.right(90);
    t.forward(Y_RANGE_UPP * 2);

    # set turtle's coordinates to starting position
    t.penup();
    t.goto(0, 0)
    t.pendown()

def drawSine(t):
    """
    description:
        use turtle to draw sin(x)
    args: 
        t: turtle object
    """

    # set turtle's coordinates to starting position
    t.penup();
    t.goto(0, 0)
    t.pendown()
    t.color('blue')

    for x in range(0, 361):
        x = myRadians(x) 
        y = mySine(x) # y = math.sin(x)
        t.goto(x, y)

        # debug
        # print('x:', round(x, 3), 'y:',  round(y, 3))

    t.penup();

def drawCosine(t):
    """
    description:
        use turtle to draw cos(x)
    args: 
        t: turtle object
    """

    # set turtle's coordinates to starting position
    t.penup();
    t.goto(0, 0)
    t.pendown()
    t.color('red')

    for x in range(0, 361):
        x = myRadians(x)
        y = myCosine(x) # y = math.cos(x)
        t.goto(x, y)

        # debug
        # print('x:', round(x, 3), 'y:',  round(y, 3))

    t.penup();

def main():
    window = turtle.Screen()
    franklin = turtle.Turtle()

    setUpWindow(window)
    setUpTurtle(franklin)
    
    drawSine(franklin)
    drawCosine(franklin)

    window.exitonclick()

    # debug sine(x)
    print('\nsin(x) = mySine(x) = math.sin(x)')
    for x in range(0, 361, 30):
        print('sin(' + str(x) + ')', '=', round(mySine(math.radians(x)), 3), '=', round(math.sin(math.radians(x)), 3))

    # debug cosine(x)
    print('\ncos(x) = myCosine(x) = math.cos(x)')
    for x in range(0, 361, 30):
        print('cos(' + str(x) + ')', '=', round(myCosine(math.radians(x)), 3), '=', round(math.cos(math.radians(x)), 3))

    # debug radians(x)
    print('\nmyRadians(x) = math.radians(x)')
    for x in range(0, 361, 30):
        print(round(myRadians(x), 3), '=', round(math.radians(x), 3))

main()
