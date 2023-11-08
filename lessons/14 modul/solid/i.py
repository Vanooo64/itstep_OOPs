from abc import ABC, abstractmethod


class WalkAble(ABC):
    @abstractmethod
    def walk(self):
        pass


class FlyAble(ABC):
    @abstractmethod
    def fly(self):
        pass

class EatAble:
    def eat(self):
        print(f"Їсти! {self.__class__.__name__}")


class Ostriche(WalkAble,EatAble):

    def walk(self):
        print("Ostriche is walking")


class Eagle(WalkAble, FlyAble, EatAble):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")

# Create instances and call methods
try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj.eat()
    obj2 = Ostriche()
    obj2.walk()
    obj2.eat()

    obj2.fly()
except Exception as e:
    print(e)