class Circle:

    def __init__(self, center, point):
        self.center = center
        self.point = point

    def getCircumference(self):
        x1, y1 = self.center
        x2, y2 = self.point
        
        # radius = sqrt((x2 - x1)^2 - (y2 - y1)^2)
        radius = abs((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
        # diameter = radius * 2
        diameter = radius * 2
        # circumference = pi * diameter
        circumference = 3.14 * diameter
        return circumference

    def __str__(self):
        circumference = self.getCircumference()
        return "The circumference of this circle is " + str(circumference)

my_circle = Circle((0, 0), (2, 4))
print(my_circle) # prints out __str__ method of Circle class
