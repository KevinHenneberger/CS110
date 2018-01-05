import turtle

def applyRules(char):
    return_str = ""
    if(char == "X"):
        return_str = "[X+YFB"
    elif(char == "F"):
        return_str = "F]X-Y"
    elif(char == "B"):
        return_str = "BX"
    else:
        return_str = char

    return return_str

def process(old_string):
    new_str = ''
    for c in old_string:
        new_str += applyRules(c)
    return new_str

def createLSystem(iterations, axiom):
    start_string = axiom
    end_string = ""
    for i in range(iterations):
        end_string = process(start_string)
        start_string = end_string
    return end_string

def drawLSystem(string, dist, deg):
    snappy = turtle.Turtle()
    snappy.speed(0)
    sn = turtle.Screen()

    positions = []

    for instruction in string:
        if (instruction == 'F'):
            snappy.forward(dist)
        elif (instruction == '-'):
            snappy.right(deg)
        elif (instruction == '+'):
            snappy.left(deg)
        elif (instruction == 'B'):
            snappy.right(180)
            snappy.forward(dist)
        elif (instruction == '['):
            x = snappy.xcor()
            y = snappy.ycor()
            d = snappy.heading()
            state = [x, y, d]
            positions.append(state)
        elif (instruction == ']'):
            if (len(positions) != 0):
                state = positions.pop(0)
                x = state[0]
                y = state[1]
                d = state[2]

                snappy.setheading(d)
                snappy.goto(x, y)

    sn.exitonclick()

def main():
    final_str = createLSystem(8, "F")
    drawLSystem(final_str, 10, 90)

main()
