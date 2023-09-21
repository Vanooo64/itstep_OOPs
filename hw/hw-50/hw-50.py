# #                       Домашня робота №50 ООП. Створення найпростіших класів.
# # Завдання 1.
# # Створіть клас Circle (Коло) із конструктором (метод __init__), у якому вказується його радіус, по замовчуванню він дорівнює 1.
# # Реалізуйте метод  __str__ (або__repr__), що повертає рядкове представлення для друку даного об’єкта.
# # Визначити такі методи:
# # •	метод для обчислення площі круга.
# # •	метод для обчислення довжини кола
# # Перевірити і заскрінити роботу програми:
# # •	створити один об’єкт (екземпляр) класу - коло з  радіусом 2, а другий – з радіусом 3.
# # •	роздрукувати ці об’єкти кола за допомогою print
# # •	викликати метод для обчислення площі круга для першого кола.
# # •	викликати метод для обчислення довжини кола для іншого кола.
#
class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __str__(self):
        return f"Circle {self.radius}"

    def area_circle(self):
        return 3.14159 * (self.radius)**2

    def length_circuit(self):
        return 2 * 3.14159 * self.radius


c1 = Circle(2)
c2 = Circle(3)
print(c1)
print(c2)

print(f"Площа кола = {c1.area_circle()}")
print(f"Довжини кола = {c1.length_circuit()}")

print(f"Площа кола = {c2.area_circle()}")
print(f"Довжини кола = {c2.length_circuit()}")

# Завдання 2.
# •	Реалізуйте клас Car (Автомобіль) із такими властивостями-атрибутами: назва моделі, рік випуску, виробник, об’єм двигуна, колір машини, ціна.
# •	Реалізуйте конструктор __init__ для класу та метод __str__.
# •	Реалізуйте метод для зміни кольору машини.
# •	Реалізуйте метод для зміни ціни машини.
# •	Додайте атрибут (поле) total класу, у якому буде міститись сумарна кількість створених об’єктів-автомобілів у програмі.
# •	Реалізуйте метод, який через об’єкт повертає значення атрибуту total класу Car.
# На кожному кроці протестуйте виконання.

class Car:
    total = 0

    def __init__(self, model_name, year, manufacturer, engine_capacity, color, price):
        self.model_name = model_name
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
        Car.total += 1

    def __str__(self):
        return f"Клас Car:  назва моделі - {self.model_name}, рік випуску - {self.year}, виробник - {self.manufacturer}, об’єм двигуна - {self.engine_capacity}, колір машини - {self.color}, ціна {self.price}"

    def total_object(self):
        return Car.total

    def color_change(self, new_color):
        self.color = new_color

    def price_change(self, new_price):
        self.price = new_price

car1 = Car('BMW', 2023, "Germany", 2.5, "black", 220000)
print(car1)
car1.color_change('white')
print(car1)
car1.price_change('215000')
print(car1)

car2 = Car('ZAZ', 2012, "Ukranian", 1.6, "black", 220000)
print(f"Сумарна кількість створених об’єктів-автомобілів у програмі = {Car.total}")

print(f"Значення атрибуту total класу Car = {car2.total_object()}")
