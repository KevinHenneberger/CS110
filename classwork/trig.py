import math

def toFixed(x, c):
    x = str(x)
    l = len(x)

    return x + (' ' * (c - l))

def main():

    angles = [x for x in range(361) if x % 30 == 0 or x % 45 == 0]

    print('-' * 25)
    print('|', toFixed('x', 3), '|', toFixed('sin(x)', 6), '|', toFixed('cos(x)', 6), '|')
    print('-' * 25)

    for x in angles:
        print('|', toFixed(x, 3), '|', toFixed(round(math.sin(math.radians(x)), 3), 6), '|', toFixed(round(math.cos(math.radians(x)), 3), 6), '|')

    print('-' * 25)

main()
