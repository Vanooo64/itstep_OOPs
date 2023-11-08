from  abc import ABC, abstractmethod

class Component(ABC): #інтерфейс для коробок і продуктів

    @abstractmethod
    def execute(self) -> float:
        pass

class Product(Component): #клас листка для продуктів або компонентів

    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def execute(self) -> float:
        return self._cost


class Box(Component): #композит

    def __init__(self, name):
        self._name = name
        self._products = []

    def add(self, c: Component): #додаемо до списку self._products продукти і компоненти
        self._products.append(c)

    def remove(self, c: Component):
        self._products.remove(c)

    def execute(self) -> float: #повертає суму ціни вмісту котобок
        cost = 0
        for children in self._products:
            print(children._name)
            cost_children = children.execute()
            cost += cost_children
        return cost


box_1 = Box("box1")
box_2 = Box("box2")
box_3 = Box("box3")
product1 = Product('Lg', 200)
product2 = Product('Iphone15', 1500)
product3 = Product('SamsungA12', 300)
product4 = Product('Other', 10)

box_1.add(product1)
box_1.add(box_2)
box_2.add(product2)
box_2.add(product3)
box_2.add(box_3)
box_3.add(product4)

print(box_1.execute())




