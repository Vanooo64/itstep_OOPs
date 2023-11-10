from abc import ABC, abstractmethod

class IShape(ABC):

    @abstractmethod
    def get_area(self) -> float:
        pass
    

class Shape(IShape):
    
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self) -> float:
        pass

    def info(self):
        print(f"Створено фігуру {self.name}")

class Square(Shape):

    def __init__(self, side: float, name: str) -> None:
        super().__init__(name)
        self.side = side

    def info(self):
        print(f"Створено фігуру {self.name}")

    def get_area(self) -> float:
        return self.side ** 2

    def __str__(self):
        return self.name


class Circle(Shape):
    def __init__(self, radius: float, name: str) -> None:
        super().__init__(name)
        self.radius = radius

    def info(self):
        print(f"Створено фігуру {self.name}")

    def get_area(self) -> float:
        return 3.14 * self.radius ** 2

    def __str__(self):
        return self.name


class Pizza:

    def __init__(self, price: float, shape: IShape) -> None:
        self._price = price
        self._shape = shape

    def get_price(self) -> float:
        return self._price

    def get_shape_class(self) -> str:
        return str(self._shape)

    def cut_pizza(self):
        print(f"{self.__class__.__name__}")

square = Square(5, "Квадрат_1")
circle = Circle(3, "Коло_1")

print(f"Площа {square.name}: {square.get_area()}")
print(f"Площа {circle.name}: {circle.get_area()}")

pizza_square = Pizza(10, square)
print(f"Ціна піци з квадратною формою: {pizza_square.get_price()}")
print(f"Форма піци з квадратною формою: {pizza_square.get_shape_class()}")

pizza_circle = Pizza(12, circle)
print(f"Ціна піци з круглою формою: {pizza_circle.get_price()}")
print(f"Форма піци з круглою формою: {pizza_circle.get_shape_class()}")

pizza_square.cut_pizza()
pizza_circle.cut_pizza()













