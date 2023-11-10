from abc import ABC, abstractmethod

class HotDog(ABC): #мета клас для створення класичних хотдогів і кастомних

    def __init__(self, name, bread, sausage, toppings):
        self.name = name
        self.bread = bread
        self.sausage = sausage
        self.toppings = toppings
        self.price = self.calculate_price()

    @abstractmethod
    def calculate_price(self):
        pass

class StandardHotDog(HotDog): # стандартний хотдог

    def __init__(self, name, bread, sausage, toppings):
        super().__init__(name, bread, sausage, toppings)

    def calculate_price(self):
        if self.name == "Класичний":
            return 45
        elif self.name == "Чікен":
            return 65
        elif self.name == "Чілі":
            return 55
        else:
            raise ValueError("Невідомий стандартний рецепт хот-догу")

    def __str__(self):
        return (f"Додано {self.name} хот-дог, його ціна {self.calculate_price()} гривень")


class CustomHotDog(HotDog): # кастомний хотдог

    def __init__(self, name, bread, sausage, toppings, kiosk):
        self.name = name
        self.bread = bread
        self.sausage = sausage
        self.toppings = toppings
        self.kiosk = kiosk
        self.price = self.calculate_price()

    def calculate_price(self):
        # Початкова ціна на основі виду хліба та сосиски
        price = self.kiosk.toppings_prices.get(self.bread, 0) + self.kiosk.toppings_prices.get(self.sausage, 0)

        # Додавання ціни за всі топінги
        for topping in self.toppings:
            price += self.kiosk.toppings_prices.get(topping, 0)

        return price

    def apply_discount(self, percentage=15): # Розрахунок знижки у відсотках, початкова 15%
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount

    def __str__(self):
        return (f"Додано {self.name} хот-дог, його ціна {self.calculate_price()} гривень")

class DiscountManager: #клас для знижок
    def __init__(self):
        self.discount_percentage = 15  # Початкова величина знижки у відсотках

    def apply_discount(self, hot_dog):
        total_hot_dogs = len(hot_dog.kiosk.custom_hot_dogs) + len(hot_dog.kiosk.standard_hot_dogs) + 1  # +1 зараз, оскільки створюється новий хот-дог

        if total_hot_dogs >= 11:
            hot_dog.apply_discount(40)
        elif total_hot_dogs >= 8:
            hot_dog.apply_discount(25)
        elif total_hot_dogs >= 4:
            hot_dog.apply_discount(self.discount_percentage)


class Kiosk():

    def __init__(self):
        self.standard_hot_dogs = [
            StandardHotDog("Класичний", "Багет", "Варені сосиски", ["Огірок", "Кетчуп", "Майонез"]),
            StandardHotDog("Чікен", "Багет", "Курячі сосиски", ["Салат", "Огірок", "Майонез"]),
            StandardHotDog("Чілі", "Багет", "Кебаб", ["Чілі", "Огірок", "Кетчуп"]),
        ]
        self.toppings_prices = {
            "Панчіхо": 20,
            "Багет": 15,
            "Огірок": 5,
            "Кетчуп": 3,
            "Майонез": 3,
            "Солодка цибуля": 8,
            "Халапеньйо": 8,
            "Чілі": 8,
            "Солоний огірок": 5,
            "Варені сосиски": 25,
            "Курячі сосиски": 25,
            "Кебаб": 35,
            "Салат": 10
        }
        self.custom_hot_dogs = []  # список з кількістю хотдогів
        self.discount_manager = DiscountManager()



    def get_hot_dog(self, name):  # створення класичного хотдогу
        for hot_dog in self.standard_hot_dogs:
            if hot_dog.name == name:
                return hot_dog
        return None

    def create_custom_hot_dog(self, name, bread, sausage, toppings):
        custom_hot_dog = CustomHotDog(name, bread, sausage, toppings, self)
        self.custom_hot_dogs.append(custom_hot_dog)

        self.discount_manager.apply_discount(custom_hot_dog)

        self.custom_hot_dogs.append(custom_hot_dog)
        return custom_hot_dog


    def save_to_file(self, hot_dog): #метод для запису у файл
        with open('orders.txt', 'a') as file:
            file.write(f"{hot_dog}\n")
            print(f"Замовлення збережено у файлі 'orders.txt'.")



# kiosk = Kiosk() # створюємо клас, для створення хотдогів
#
# # Створення класичних хот-догів
# classic_hot_dog = kiosk.get_hot_dog("Класичний")
# chiken_hot_dog = kiosk.get_hot_dog("Чікен")
# chilli_hot_dog = kiosk.get_hot_dog("Чілі")
#
#
# print(classic_hot_dog)
# print(chiken_hot_dog)
# print(chilli_hot_dog)
#
# kiosk.save_to_file(classic_hot_dog) #запиc у файл
# kiosk.save_to_file(chiken_hot_dog) #запиc у файл
# kiosk.save_to_file(chilli_hot_dog) #запиc у файл
#
#
# # Створення кастомного хот-дога
# custom_hot_dog = kiosk.create_custom_hot_dog("Кастомний", "Панчіхо", "Кебаб", ["Огірок", "Салат", "Солодка цибуля", ])
# # Вивід інформації про кастомний хот-дог
# print(custom_hot_dog)
#
# kiosk.save_to_file(custom_hot_dog) #запиc у файл

# Створення замовлення на 10 хот-догів
kiosk = Kiosk()

for i in range(10):
    custom_hot_dog = kiosk.create_custom_hot_dog(f"Кастомний_{i+1}", "Панчіхо", "Кебаб", ["Огірок", "Салат", "Солодка цибуля"])
    print(custom_hot_dog)
    custom_hot_dog.apply_discount()  # Вручну викликаємо метод apply_discount












