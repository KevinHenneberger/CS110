import random
import turtle
import os

def main():

    """
    ======================
    Part A
    ======================
    """
    x = random.randrange(1, 10)
    print(x)

    """
    ======================
    Part B
    ======================
    """
    window = turtle.Screen()
    window.bgcolor('lightblue')

    michelangelo = turtle.Turtle()
    leonardo = turtle.Turtle()

    michelangelo.color('orange')
    leonardo.color('blue')

    michelangelo.shape('turtle')
    leonardo.shape('turtle')

    michelangelo.up()
    leonardo.up()

    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)

    # Method #1
    michelangelo.forward(random.randrange(1, 300))
    leonardo.forward(random.randrange(1, 300))

    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)

    # Method #2
    for steps in range(10):
        michelangelo.forward(random.randrange(0, 30))
        leonardo.forward(random.randrange(0, 30))

    michelangelo.up()
    leonardo.up()
    michelangelo.goto(-250, 100)
    michelangelo.down()
    leonardo.down()

    """
    ======================
    Part C
    ======================
    """
    # Equilateral Triangle
    michelangelo.forward(100)
    michelangelo.left(120)
    michelangelo.forward(100)
    michelangelo.left(120)
    michelangelo.forward(100)
    michelangelo.left(120)

    michelangelo.up()
    leonardo.up()
    michelangelo.goto(-50, 100)
    michelangelo.down()
    leonardo.down()

    # Square
    michelangelo.forward(100)
    michelangelo.left(90)
    michelangelo.forward(100)
    michelangelo.left(90)
    michelangelo.forward(100)
    michelangelo.left(90)
    michelangelo.forward(100)
    michelangelo.left(90)

    michelangelo.up()
    leonardo.up()
    michelangelo.goto(150, 100)
    michelangelo.down()
    leonardo.down()

    # Hexagon
    michelangelo.forward(100)
    michelangelo.left(60)
    michelangelo.forward(100)
    michelangelo.left(60)
    michelangelo.forward(100)
    michelangelo.left(60)
    michelangelo.forward(100)
    michelangelo.left(60)
    michelangelo.forward(100)
    michelangelo.left(60)
    michelangelo.forward(100)
    michelangelo.left(60)

    michelangelo.up()
    leonardo.up()
    michelangelo.goto(-50, -200)
    michelangelo.down()
    leonardo.down()

    # Octagon
    michelangelo.forward(100)
    michelangelo.left(45)
    michelangelo.forward(100)
    michelangelo.left(45)
    michelangelo.forward(100)
    michelangelo.left(45)
    michelangelo.forward(100)
    michelangelo.left(45)
    michelangelo.forward(100)
    michelangelo.left(45)
    michelangelo.forward(100)
    michelangelo.left(45)
    michelangelo.forward(100)
    michelangelo.left(45)
    michelangelo.forward(100)
    michelangelo.left(45)    

    window.exitonclick()

    """
    ======================
    Part D
    ======================
    """
    os.system('man man')
    os.system('man pwd')
    os.system('man mkdir')
    os.system('man rm')
    os.system('man cd')
    os.system('man ls')
    os.system('man mv')
    os.system('man cp')
    os.system('man python3')

main()
