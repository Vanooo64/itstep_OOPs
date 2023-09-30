
# Завдання 2
# Створіть клас Circe (Коло).
# Для даного класу реалізуйте ряд перевантажених операторів:
# - перевірка на рівність радіусів двох кіл (операція ==);
# - порівняння довжини двох кіл (операції », <=, *=);
# - пропорційна зміна розмірів кола шляхо м зміни його радіусу (операції +, -, +=, -=).
# - реалізуйте магічний метод stri repr, а також метод int(який повертає цілу частину довжини кола).

from task1 import Point
from math import pi, trunc


class Circle:

    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.point = Point(x, y)

    def __repr__(self):
        return f"Circle r={self.radius} wiht point {self.point}"

    # - перевірка на рівність радіусів двох кіл (операція ==);
    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other): # коли робиш порівнння не =
        return not self.__eq__(other) #логіка не дорівнює

    # - порівняння довжини двох кіл (операції », <=, *=);
    def __ge__(self, other):
        return self.radius >= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    # - пропорційна зміна розмірів кола шляхо м зміни його радіусу (операції +, -, +=, -=).
    def __iadd__(self, other):
        # return Circle(self.radius + other, self.point.x, self.point.y) #повертае новий обект
        self.radius += other # аналогічно, але повертае той самий обект
        return self

    def __int__(self):
        l = 2 * pi * self.radius
        return trunc(l) #повертає цілу частину довжини кола

    def __len__(self):
        return self.__int__()

    def __float__(self):
        return 2 * pi * self.radius


c1 = Circle(1, 0, 0)
c2 = Circle(2, 1, 1)
# print(c1)
# print(c2)
# # print(c1 == c2)
# # print(c1 != c2)
# print(c1 >= c2)
# print(c1 < c2)

# print(c1, id(c1))
# c1 += 5
# print(c1, id(c1))

print(int(c1))

print(len(c1))

print(float(c1))


