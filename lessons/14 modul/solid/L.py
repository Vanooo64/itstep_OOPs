from typing import List
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set(self, width, height):
        self.width = width
        self.height = height

    # Calculate rectangle area
    def calculate_area(self):
        return self.width * self.height


# Square class, inherits from Rectangle
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


# Function to calculate total area of multiple rectangles
def calculate_total_area(shapes: list[Shape]) -> float:
    total_area = 0
    for obj in shapes:
        total_area += obj.calculate_area()
    return total_area


r = Rectangle(5, 6)
s = Square(10)
c = Circle(1)
shapes = [r, s, c]
print(calculate_total_area(shapes))
