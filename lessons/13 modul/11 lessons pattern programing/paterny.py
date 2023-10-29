# from abc import ABCMeta, abstractmethod
#
#
# class Pet(metaclass=ABCMeta):
#
#     def __init__(self, name):
#         self._name = name
#
#     @abstractmethod  # при створенні дочерного класу забовязуе розробника імплементувати всі @abstractmethod, або буде помилка
#     def voice(self):
#         pass
#
#
# class LogMixin:  # Миксина яка використовуеться у двох класах
#
#     def info(self):
#         print(f"Class {self.__class__.__name__} - {self._name}")
#
#
# class Cat(Pet, LogMixin):
#
#     def voice(self):
#         print('May-may')
#
#
# class Dog(Pet, LogMixin):
#
#     def voice(self):
#         print('Гав-Гав')
#
#
# c = Cat('Pushok')
# c.info()
# c.voice()
#
# d = Dog('Rex')
# d.info()
# d.voice()

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetr(self) -> float:
        pass

    # @abstractmethod
    def description(self) -> float:
        print(f"{self.__class__.__name__} - {self.color}")


class Rectangel(Shape):
    def __init__(self, width, height, color):
        super().__init__(color) # викликаемо з батькіського класу
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimetr(self) -> float:
        return 2 * (self.width * self.height)


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color) # викликаемо з батькіського класу
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimetr(self) -> float:
        return 2 * 3.14 * self.radius


r = Rectangel(3,4,'black')
print(r.area())
print(r.perimetr())
r.description()

c = Circle(5, "red")
print(c.area())
print(c.perimetr())
c.description()

