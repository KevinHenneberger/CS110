import turtle

def applyRules(char):
    return_str = ""
    if(char == "X"):
        return_str = "X+YF"
    elif(char == "Y"):
        return_str = "FX-Y"
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

    for instruction in string:
        if (instruction == 'F'):
            snappy.forward(dist)
        elif (instruction == '-'):
            snappy.right(deg)
        elif (instruction == '+'):
            snappy.left(deg)

    sn.exitonclick()

def main():
    iters = int(input("Number of iterations: "))
    final_str = createLSystem(iters, "FX")
    distance = int(input("How far forward?: "))
    degree = int(input("How much to turn?: "))
    drawLSystem(final_str, distance, degree)

main()
