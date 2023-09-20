# Завдання 1.
# Напишіть клас під назвою Rectangle для визначення площі прямокутника за введеними довжиною та шириною сторін.
# Клас прямокутника має містити метод, який обчислює площу прямокутника.

# class Rectangel:
#     length = 5
#     width = 10
#
#     def area(self):
#         return self.length * self.width
#
#
# if __name__ == '__main__':
#     obj = Rectangel()
#     obj.length = 3
#     obj.width = 9
#     obj1 = Rectangel()
#     square = obj.area()
#     print(f"{square= }")
#     print(Rectangel.length, Rectangel.width)


# class Rectangel:
#     name = 'Rectangel-area'  # змінна класу, атрибут або поле класу
#
#     def __init__(self, length, width): #ініціалізатор
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#
# obj = Rectangel(30, 50)
# print(obj.name)
# print(obj.length, obj.width)
# print(obj.area())
#
# obj.area()  # Rectangel.area(obj) - аналогычний виклик


# class Rectangel:
#     name = 'Rectangel-area'  # змінна класу, атрибут або поле класу
#
#     def __init__(self, length, width): #ініціалізатор
#         self.length = length
#         self.width = width
#
#     def __str__(self): #для представлення у строковому вигляді для користувача, викликаетсься автоматично при виклику print(obj)
#         return f"Rectangel {self.width}x{self.length}={self.area()}"
#
#     def area(self):
#         return self.length * self.width
#
#
# obj = Rectangel(30, 50)
# print(obj)
# print(obj.name)
# print(obj.length, obj.width)
# print(obj.area())
#
# obj.area()  # Rectangel.area(obj) - аналогычний виклик


# class Rectangel:
#     name = 'Rectangel-area'  # змінна класу, атрибут або поле класу
#
#     def __init__(self, length, width): #ініціалізатор
#         self.length = length
#         self.width = width
#
#     def __str__(self): #для представлення у строковому вигляді для користувача, викликаетсься автоматично при виклику print(obj)
#         return f"Rectangel {self.width}x{self.length}"
#
#     def area(self):
#         return self.length * self.width
#
#     def info(self):
#         print(f'Info: {self.width} x {self.length} = {self.area()}')
#
#     def change_atr(self):
#         new_length = int(input('Введіть нову довжину: '))
#         new_width = int(input('Введіть нову ширину: '))
#         self.length = new_length
#         self.width = new_width
#         print('Змінено атрибути обєкта')
#
# obj = Rectangel(30, 50)
# print(obj)
# obj.info()
# print(obj.area())
#
# obj.change_atr()
# obj.info()
# print(obj.area())

# Завдання 2.
# Створіть клас «Місто». Збережіть у класі: назву міста, назву регіону, назву країни, кількість жителів у місті, поштовий індекс міста.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
# До вже реалізованого класу «Місто» додайте конструктор та str метод.
# До вже реалізованого класу додайте статичний метод, який під час виклику повертає кількість створених об’єктів класу «Місто».

# class City:
#     count = 0
#
#     def __init__(self, name, region, country, population, index):
#         self.name = name
#         self.region = region
#         self.country = country
#         self.population = population
#         self.index = index
#         City.count += 1
#
#     def __str__(self):
#         return f"City {self.name, self.population, self.index}"
#
#     def get_count_cities(self):
#         return City.count
#
# s1 = City('I-F', 'West', "UA", 470, 76000)
# s2 = City('Kiev', 'Centeral', 'UA', 5000, 86000)
# s3 = City('Lviv', 'West', 'UA', 800, 89000)
#
# lst = [s1, s2, s3] #cобекти можна зберізати у списках або словниках
# for s in lst:
#     print(s)
#
# print(f"{s2.count=}")
# City.count = 2 #перепризначення атрибуту класу
# print(f"{s1.get_count_cities()}")

# class City:
#     count = 0
#
#     def __init__(self, name, region, country, population, index):
#         self.name = name
#         self.region = region
#         self.country = country
#         self.population = population
#         self.index = index
#         City.count += self.population
#
#     def __str__(self):
#         return f"City {self.name, self.population, self.index}"
#
#     def get_count_cities(self):
#         return City.count
#
#
# s1 = City('I-F', 'West', "UA", 470, 76000)
# s2 = City('Kiev', 'Centeral', 'UA', 5000, 86000)
# s3 = City('Lviv', 'West', 'UA', 800, 89000)
#
# lst = [s1, s2, s3]  # cобекти можна зберізати у списках або словниках
# for s in lst:
#     print(s)
#
# print(f"{s2.count=}")
# City.count = 2  # перепризначення атрибуту класу
# print(f"{s1.get_count_cities()}")

# # Завдання 3.
# # Реалізуйте клас MoneyBox для роботи з віртуальною скарбничкою. Кожна скарбничка має обмежену місткість, яка виражається цілим числом
# # n - кількістю монет, які можна покласти в скарбничку. Клас повинен підтримувати інформацію про кількість монет в скарбничці,
# # надавати можливість додавати монети в скарбничку і дізнаватися, чи можна додати в скарбничку ще якусь кількість монет, не перевищуючи
# # її місткість. Клас повинен мати наступний вигляд
# # class MoneyBox:
# # def __init__(self, capacity):
# # # Конструктор з аргументом - місткість скарбнички
# # def can_add(self, v):
# # # True, якщо можна додати v монет, False інакше
# # def add(self, v):
# #
# # # Покласти v монет в скарбничку
# # При створенні скарбнички, число монет в ній дорівнює 0. Врахуйте, що метод add(self, v) буде викликатися лише тоді, якщо can_add(self, v)
# # повертає True. Дані вводиться користувачем в такому порядку: n - місткість скарбнички, m - скільки монет поклали в скарбничку, k - кількість
# # монет, які хочуть покласти в скарбничку. Результатом має бути одне з двох значень: True чи False.
#
# class MoneyBox:
#     def __init__(self, capacity):  # Конструктор з аргументом - місткість скарбнички
#         self.capacity = capacity
#         self.count = 0
#
#     def can_add(self, v):  # True, якщо можна додати v монет, False інакше
#         if self.count + v <= self.capacity:
#             return True
#         return False
#
#     def add(self, v):  # Покласти v монет в скарбничку
#         if self.can_add(v):
#             self.count += v
#         else:
#             print(f'Скарбничка переповнена, не можна додати {v} монет')
#
# box = MoneyBox(capacity=10)
# box.add(6)

