# # Завдання 1.
# # Розробити систему для управління продуктами в магазині з можливістю створення ієрархії категорій і товарів.
# # Магазин має категорії, які можуть містити в собі підкатегорії або окремі товари. Кожен товар має свою назву та ціну.
# # Завдання полягає у створенні класів Товар (Product) та Категорія (Category). Кожен об'єкт класу Товар має метод для отримання ціни товару.
# # Кожен об'єкт класу Категорія має методи для додавання та видалення підкатегорій або товарів, а також метод для отримання загальної
# # ціни всіх товарів у категорії та її підкатегоріях. Також треба розробити клас Магазин (Store), який буде мати методи для створення
# # ієрархії категорій і товарів, а також метод для обчислення загальної ціни всіх товарів у магазині.
# # Протестуйте роботу.
#
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def get_total_price(self):
        pass

class Product(Component):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_price(self):
        return self.price

class Category(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_total_price(self):
        total_price = sum(child.get_total_price() for child in self.children)
        return total_price

class Store:
    def __init__(self):
        self.root_category = Category("Root")

    def create_category_hierarchy(self, category, parent_category=None):
        if parent_category is None:
            parent_category = self.root_category
        parent_category.add_child(category)

    def create_product(self, product, category):
        category.add_child(product)

    def get_total_price(self):
        return self.root_category.get_total_price()

# Приклад використання

store = Store()

# Створюємо категорії
electronics = Category("Electronics")
clothing = Category("Clothing")
appliances = Category("Appliances")

# Створюємо підкатегорії
laptops = Category("Laptops")
smartphones = Category("Smartphones")

# Додаємо підкатегорії до головних категорій
store.create_category_hierarchy(electronics)
store.create_category_hierarchy(clothing)
store.create_category_hierarchy(appliances)

store.create_category_hierarchy(laptops, electronics)
store.create_category_hierarchy(smartphones, electronics)

# Створюємо товари
product1 = Product("Macbook Air", 1000)
product2 = Product("Macbook Pro", 1200)
product3 = Product("Iphone 12", 500)
product4 = Product("Iphone 13", 600)

# Додаємо товари до категорій
store.create_product(product1, laptops)
store.create_product(product2, laptops)
store.create_product(product3, smartphones)
store.create_product(product4, smartphones)

# Отримуємо загальну ціну всіх товарів у магазині
total_price = store.get_total_price()
print(f"Total price of all products in the store: ${total_price}")


# # Завдання 2.
# # Розробити систему для ведення каналу на платформі відеохостингу з можливістю підписки на канал та сповіщення підписників про нові відео, які були викладені на каналі. Канал може мати декілька підписників, які отримують сповіщення про нові відео, коли вони стають доступними.
# # Канал повинен мати методи для додавання і видалення підписників, а також метод для публікації нового відео. Підписник повинен мати метод, що відповідає за отримання сповіщення про нове відео. Також треба реалізувати надсилання сповіщень підписникам про нове відео.
# # Протестуйте роботу.
#
# from abc import ABC, abstractmethod
#
#
# class Subscriber(ABC):
#     @abstractmethod
#     def update(self, video):
#         pass
#
#
# class Channel:        #  додавання і видалення підписників   публікації нового відео
#     def __init__(self):
#         self.subscribers = set()   # множина підписників
#         self.videos = []           # список відео
#
#     def add_subscriber(self, subscriber):    #додавання підписників
#         self.subscribers.add(subscriber)
#
#     def remove_subscriber(self, subscriber):  #видалення підписників
#         self.subscribers.remove(subscriber)
#
#     def publishing_new_video(self, video):    # публікації нового відео
#         self.sending_notifications(video)
#         self.videos.append(video)
#
#
#     def sending_notifications(self, video):    #надсилання сповіщень підписникам про нове відео
#         for subscriber in self.subscribers:
#             subscriber.update(video)
#
#
# class User(Subscriber):
#     def __init__(self, name):
#         self.name = name
#
#     def update(self, video):
#         print(f"{self.name} отримав нове відео: {video}")
#
# # Створити канал
# channel = Channel()
#
# # Створити підписників
# user1 = User("Alice")
# user2 = User("Bob")
# user3 = User("Charlie")
#
# # Додати підписників до каналу
# channel.add_subscriber(user1)
# channel.add_subscriber(user2)
# channel.add_subscriber(user3)
#
# # Опублікувати нове відео
# channel.publishing_new_video("Video 1")
#
# # Видалити підписника
# channel.remove_subscriber(user2)
#
# # Опублікувати ще одне нове відео
# channel.publishing_new_video("Video 2")

# Завдання 3
# Реалізуйте патерн Command з деякої предметної області (оберіть самі)  або виконайте  наступне завдання.
# Розробити систему замовлення їжі в ресторані з можливістю відміни останнього замовлення. Клієнт може додавати різні елементи до замовлення, такі як страви, напої, десерти тощо. Також клієнт може відміняти останнє додане до замовлення елемент. Завдання полягає у створенні інтерфейсу Command з абстрактними методами execute(), який виконує деяку операцію, і undo(), який відміняє цю операцію.
# Розробити клас замовлення Order, що виступає як отримувач команди і має методи place_order() і cancel_order(), які відповідають за розміщення замовлення та його відміну.

from abc import ABC, abstractmethod

class Command(ABC): # абстрактний метод

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Order:
    def __init__(self):
        self.is_placed = False
        self.items = []

    def place_order(self):
        self.is_placed = True
        print("Замовлення розміщенно")

    def cancel_order(self):
        self.is_placed = False
        print("Замовлення відмінено.")

    def add_item(self, item):
        self.items.append(item)
        print(f"Елемент {item} додано до замовлення.")

    def remove_item(self, item):
        self.items.remove(item)
        print(f"Елемент {item} видалено з замовлення.")


class PlaceOrderCommand(Command): # команди для розміщення і скасування замовлень
    def __init__(self, order):
        self.order = order

    def execute(self):
        self.order.place_order()

    def undo(self):
        self.order.cancel_order()


class AddItemCommand(Command):
    def __init__(self, order, item):
        self.order = order
        self.item = item

    def execute(self):
        self.order.add_item(self.item)

    def undo(self):
        self.order.remove_item(self.item)


class RemoveItemCommand(Command):
    def __init__(self, order, item):
        self.order = order
        self.item = item

    def execute(self):
        self.order.remove_item(self.item)

    def undo(self):
        self.order.add_item(self.item)


class CommandController:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()
        else:
            print('Немає команди для відміни')

order = Order()
controller = CommandController()

# Створюємо команди
place_order_command = PlaceOrderCommand(order)
add_item_command = AddItemCommand(order, "Біг мак меню")
remove_item_command = RemoveItemCommand(order, "Біг мак меню")

# Виконуємо команди
controller.execute_command(place_order_command)  # Розміщуємо замовлення
controller.execute_command(add_item_command)      # Додаємо елемент
controller.execute_command(remove_item_command)   # Видаляємо елемент

# Відмінюємо останню команду (видалення елемента)
controller.undo_last_command()

# Відмінюємо ще раз (додавання елемента)
controller.undo_last_command()














        


