from math import pi

class AreaUnknownError(AttributeError):
    def __str__(self):
        return "This Object has no known area"


class Shape():
    def __init__(self, coord, lines):
        try:
            self.x, self.y = coord
            self.lines = [float(line) for line in lines]
        except:
            raise TypeError("Illegal init values")
        
    def circumference(self):
        return sum(self.lines)
    
    def area(self):
        raise AreaUnknownError
        
    def __add__(self, other):
        return self.area() + other.area()
    
    def __str__(self):
        return "A {} with circumference {}".format(type(self).__name__, self.circumference())
    
    def __eq__(self, other):
        return self.lines == other.lines
    
class Circle(Shape):
    def __init__(self, coord, radius):
        self.radius = radius
        lines = [2*pi*radius]
        super().__init__(coord, lines)
    
    def area(self):
        return self.lines[0]**2
    
class Rectangle(Shape):
    def __init__(self, coord, width, height):
        self.width = float(width)
        self.height = float(height)
        lines = [width, height, width, height]
        super().__init__(coord, lines)
    
    def area(self):
        return self.width*self.height