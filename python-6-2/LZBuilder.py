# LZBuilder.py
import math

class LZBuilder:
    def __init__(self, radius=0):
        """Constructor with a default radius of 0 if no value is provided."""
        self.radius = radius

    def setRadius(self, radius):
        """Sets the radius of the landing zone."""
        self.radius = radius

    def getArea(self):
        """Returns the area of the landing zone (πr²)."""
        return math.pi * self.radius ** 2

    def getRadius(self):
        """Returns the radius of the landing zone."""
        return self.radius

    def getDiameter(self):
        """Returns the diameter of the landing zone (2r)."""
        return self.radius * 2

    def getCircumference(self):
        """Returns the circumference of the landing zone (2πr)."""
        return 2 * math.pi * self.radius
