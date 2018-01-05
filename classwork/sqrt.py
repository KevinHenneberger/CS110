import math

def toFixed(x, c):
    x = str(x)
    l = len(x)

    return x + (' ' * (c - l))

def sqrt(x):

    epsilon = 1e-15
    e = x

    while True:
        y = ((x / e) + e) / 2

        if abs(y - e) < epsilon:
            return round(e, 5)

        e = y

def main():
    for x in range(1, 25):
        print(toFixed(x, 2), '||', toFixed(sqrt(x), 7), '||', toFixed(round(math.sqrt(x), 5), 7))

main()
