# # Завдання 1.
# # Визначити клас Point, який представляє точку в 2D системі координат та магічні методи для налаштування поведінки класу.
# # - Метод __init__ ініціалізує атрибути х і у обʼєкта Point.
# # - Метод __str__ повертає рядкове представлення обʼєкта Point.
# # - Метод __еq__ порівнює два обʼєкти Point на рівність.
# # - Метод __add__ дозволяє додавати два обʼєкти Point шляхо м повернення нового обʼєкта Point із підсумованими координатами.
# # - Метод __len__ повертає довжину обʼєкта Point, яка обчислюється як сума абсолютних значень його координат.

class Point:
    """Клас Point2D"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x = {self.x}, y = {self.y})"

    # перевизначае рівність якшо обекти рівні. за замовченням якщо аргументи обектів однакові, повертаеться False
    def __eq__(self, other):  # other обект B
        if self.x == other.x and self.y == other.y:
            return True
        return False
        # return self.x == other.x and self.y == other.y # аналогічно

    def __add__(self, other):  # щоб додавати значення обектів A + B
        if isinstance(other, Point):  # якщо обект B является єкземляром клосу поінт
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Point(new_x, new_y)  # новий обект, якщо додаемо просто число
        elif isinstance(other, (int, float)):
            new_x = self.x + other
            new_y = self.y + other
            return Point(new_x, new_y)  # новий обект
        else:
            raise ValueError("Невірний тип операнда")

    def __radd__(self, other):
        return self.__add__(other)

    def __len__(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":


    A = Point(2, 3)  # __eq__
    B = Point(2, 3)
    print(A)
    print(B)
    print(id(A), id(B))  # 4451680208 4451679872
    print(A == B)

    A = Point(-1, 3)  # __add__
    B = Point(2, 3)
    C = A + B
    print(C)  # (x = 3, y = 6)

    C = A + 5
    print(C)  # (x = 6, y = 8)

    E = 5 + B
    print(E)  # (x = 3, y = 6)

    print(f"len A = {len(A)}")  # __len__