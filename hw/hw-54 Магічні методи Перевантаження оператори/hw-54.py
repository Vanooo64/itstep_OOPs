import math

class Vector:

    def __init__(self, x, y, z):
        # Перевірка, чи аргументи є числового типу
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
            raise ValueError('Координати повинні бути числового типу.')

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{Vector.__name__} ({self.x}, {self.y}, {self.z})"

# 1.	Реалізуйте порівняння двох векторів за рівністю їх координат (==, !=), тобто перевірити, чи мають обидва
# вектори однакові координати і повернути відповідне значення (True або False)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

# 2.	Реалізувати методи  __add__ і  __sub__ для  додавання і віднімання двох векторів відповідно (повертає
# новий вектор з координатами).

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            new_z = self.z - other.z
            return Vector(new_x, new_y, new_z)

# 3.Додатково реалізувати методи  __iadd__ і  __isub__ для перевантаження операторів присвоєння += та -+
# двох векторів відповідно.
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"Додавати можна тільки об'єкти типу Vector")
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"Додавати можна тільки об'єкти типу Vector")
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

# 4. Реалізувати метод __mul__, що повертає скалярний добуток двох векторів.

    def __mul__(self, other):
        new_x = self.x * other
        new_y = self.y * other
        new_z = self.z * other
        return Vector(new_x, new_y, new_z)

# Крім того, передбачити множення вектора v на число α як із лівого, так і з правого боку, тобто  v*α та α*v.
# Тут має повертатись той самий вектор із помноженими координатами на це число.

    def __rmul__(self, other):
        return self * other

# 6.	Реалізувати метод __len__, що повертатиме довжину вектора.
    def __len__(self): #__len__ має повертати ціле число, але обчислення довжини вектора може повертати значення типу float!!!!!
        return int(math.sqrt((self.x**2) + (self.y**2) + (self.z**2)))

# 7.	Реалізувати метод __int__, що повертатиме цілу частину довжини вектора.
    def __int__(self):
        return Vector.__len__(self)

# 8.	Реалізувати метод __neq__ , що повертатиме для вектора v протилежний вектор -v. Тобто, потрібно змінити знак всіх координат
# вектора, повертаючи вектор з оберненими значеннями координат.

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

# 9.Реалізувати методи __getitem__ і __setitem__, що дозволяють достукатись до координат вектора за допомогою індексів.
# Наприклад, ви можете використовувати v[1] для доступу до першої координати вектора, v[2] - до другої, v[3] - до третьої.

    def __getitem__(self, item): #Дозволяє отримати координату вектора за індексом
        if item == 1:
            return self.x
        elif item == 2:
            return self.y
        elif item == 3:
            return self.z
        else:
            raise ValueError ("Індекс поза діапазоном. Підтримувані індекси: 1, 2, 3")

    def __setitem__(self, key, value): #Дозволяє встановити координату вектора за індексом
        if key == 1:
            self.x = value
        elif key == 2:
            self.y = value
        elif key == 3:
            self.z = value
        else:
            raise ValueError ("Індекс поза діапазоном. Підтримувані індекси: 1, 2, 3")

# 10.	Реалізуйте метод __contains__, що дозволяє перевірити, чи міститься деяке значення у певній координаті
# у вектора і повернути відповідне значення (True або False).

    def __contains__(self, item):
        return item in (self.x, self.y, self.z)

# 11.	Реалізуйте метод  __bool__, що дозволяє перевірити, чи є вектор «істинним» (True) або «хибним» (False).
# Зокрема, вектор є «істинним», якщо його довжина не дорівнює нулю.

    def __bool__(self):
        if Vector.__len__(self) != 0:
            return True
        return False

# 12.	Зробіть об’єкти класу Vector функторами за допомогою __сall__. Логіку при виклику придумайте самі.

    def __call__(self, multiplier): #Множить кожну координату вектора на певне число (multiplier)
        self.x *= multiplier
        self.y *= multiplier
        self.z *= multiplier


v1 = Vector(1, 2, 3)
v2 = Vector(0, 0, 0)

#Множить кожну координату вектора на певне число (multiplier)
v1(2)
print(v1)

# print(v1 == v2) #порівняння двох векторів за рівністю їх координат
#
# v3 = v1 + v2  # додавання двох векторів
# print(f"v3 = {v3}")
# v4 = v1 - v2 # віднімння двох векторів
# print(v4)
#
# v1 += v3 #перевантаження операторів присвоєння
# print(v1)
#
# v1 -= v3 #перевантаження операторів присвоєння
# print(v1)
#
# v5 = v1 * v2  #скалярний добуток двох векторів
# print(v5)

# # множення вектора v на число α
# v6 = v1 * 5
# print(v6)
# v7 = 2 * v1
# print(v7)

# # Отримання довжини вектора
# v8 = len(v1)
# print("Довжина вектора:", v8)

# # Отримання довжини вектора
# v9 = int(v1)
# print("Довжина вектора:", v9)

# # Вектора v протилежний вектор -v
# v10 = -v1
# print("Вектора v протилежний вектор -v.:", v10)

# # Дозволяє отримати координату вектора за індексом
# print(v1[3], v1[2], v1[1])
#
# #Дозволяє встановити координату вектора за індексом
# v1[1] = 10
# v1[2] = 20
# v1[3] = 30
# print(v1)

# # Перевірка наявності значень у координатах вектора
# print(2 in v1)  # Перевірка наявності значення 2
# print(5 in v1)  # Перевірка наявності значення 5

# # Реалізуйте метод  __bool__, що дозволяє перевірити, чи є вектор «істинним» (True) або «хибним» (False).
# print(f"довжина вектора v1 не дорівнює нулю: {bool(v1)}")
# print(f"довжина вектора v2 не дорівнює нулю: {bool(v2)}")



