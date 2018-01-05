import turtle

def seq3np1(n):
    """
    - Return the number of iterations it takes for the 3n+1 sequence from n to terminate

    - n = number
    """

    count = 0

    while(n != 1):

        count += 1

        # if n is even...
        if(n % 2) == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    
    return count

def drawGraph(w, t, num_iterations):
    """
    - Write a function that will take an upper bound value and use the turtle graphics library to graph the number of iterations

    - w = window
    - t = turtle
    - num_iterations = number of iterations (upper bound)
    """

    # initialize world coordinates to (0, 0, 10, 10)
    w.setworldcoordinates(0, 0, 10, 10)

    # keep track of the maximum number of iterations (initialize it to zero)
    max_so_far = 0

    # use a for loop using the number of iterations
    # provides values from 1 up to (and including) the user supplied upper bound
    for start in range(1, num_iterations + 1):

        # save the result of the seq3np1 function in a variable called result
        result = seq3np1(start)

        # write a print statement that prints the value of start and the number of iterations
        print('Start:', start, 'Count:', result)

        # check result to see if it is greater than max_so_far
        if (result > max_so_far):
            # if so, update max_so_far
            max_so_far = result
     
        # update the graph on every iteration
        # x-axis max = current value of the loop iterator + 10
        # y-axis max = the max_so_far value + 10
        w.setworldcoordinates(0, 0, start + 10, max_so_far + 10)

        # graph the result with your turtle
        turtle.goto(start, result)
        turtle.dot()

        # write out the loop variable and the number of iterations only if the number of iterations is more than 100
        if (result > 100):
            turtle.write('(' + str(start) + ', ' + str(result) + ' )')

def main():

    # ask the user for a value to use for the upper bound of your range
    upper_bound = int(input('Enter an Upper Bound: '))

    # create a plotter and a window
    window = turtle.Screen()
    plotter = turtle.Turtle()
    drawGraph(window, plotter, upper_bound)
    window.exitonclick()
    
main()
