def accumulator(list): 

    accum = 0
    for i in list:
        accum += i

    return accum

def square(num):

    result = 0
    for i in range(num):
        result += num

    return result

def conditionals():

    num = int(input('Please enter a number => '))

    if num != 0:
        return 20 / num
    else:
        return 'Error, attempted to divide by zero.'

def main():

    print(accumulator(range(5)))
    print(square(5))
    print(conditionals())

main()
