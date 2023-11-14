from abc import ABC, abstractmethod


# Інтерфейсний клас "Shape"
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def fill_color(self, color):
        pass

    @abstractmethod
    def erase(self):
        pass


# Підклас "Circle" реалізує методи "draw" та "fill_color"
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

    def fill_color(self, color):
        print(f"Filling the circle with {color}")

    def erase(self):
        print("Erasing the circle")


# Підклас "Rectangle" реалізує методи "draw" та "fill_color"
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

    def fill_color(self, color):
        print(f"Filling the rectangle with {color}")

    def erase(self):
        print("Erasing the rectangle")


# Абстрактний клас "Creator"
class Creator(ABC):
    @abstractmethod
    def create_product(self):
        pass

    def render(self, color):
        product = self.create_product()
        product.draw()
        product.fill_color(color)
        product.erase()


# Конкретний творець для кола
class CircleCreator(Creator):
    def create_product(self):
        return Circle()


# Конкретний творець для прямокутника
class RectangleCreator(Creator):
    def create_product(self):
        return Rectangle()


# Створення об'єктів без тестування
circle_creator = CircleCreator()
rectangle_creator = RectangleCreator()

circle = circle_creator.create_product()
rectangle = rectangle_creator.create_product()

# Використання об'єктів
circle.draw()
circle.fill_color("blue")
circle.erase()

print()

rectangle.draw()
rectangle.fill_color("red")
rectangle.erase()






