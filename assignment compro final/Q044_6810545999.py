# Name: Inthat # Student ID: 68010545999
import math

class Shape:
    def __init__(self, color):
        self.color = color
    
    def get_area(self):
        return 0
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def get_area(self):
        return math.pi * (self.radius**2)


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height
    
shape = input("Create (circle/rectangle/triangle): ")
color = input("Enter color: ")
if shape.lower() == 'circle':
    radius = float(input("Enter radius: "))
    shape = Circle(color, radius)
    print(f"Info: Color: {shape.color}, Area: {(shape.get_area()):.2f}")
elif shape.lower() == 'triangle':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    shape = Triangle(color, base, height)
    print(f"Info: Color: {shape.color}, Area: {(shape.get_area()):.2f}")
elif shape.lower() == 'rectangle':
    width = float("Enter width: ")
    height = float("Enter height: ")
    shape = Rectangle(color, width, height)
    print(f"Info: Color: {shape.color}, Area: {(shape.get_area()):.2f}")
