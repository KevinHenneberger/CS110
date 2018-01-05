class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def main():

    p = Point(3, 4)
    q = Point(5, 2)

    print(p)
    print(q)

    print(p.distFromOrigin())
    print(q.distFromOrigin())

main()
