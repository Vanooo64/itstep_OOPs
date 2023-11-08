#                      декорування за допомогою класу
def start(func):
    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)

    return wrapper()


class MyDrcorator:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("*" * 10)
        self._func(*args, **kwargs)
        print("*" * 10)

# def f1(x):
#     print(f"Call f1 = {x**2}")
#
# f1 = MyDrcorator(f1)
#
# f1(3)


#аналогічно
@MyDrcorator
def f1(x):
    print(f"Call f1 = {x**2}")

f1(3)


#                           декоратор класу з параметрами
class MyDrcorator:
    def __init__(self, n):
        self.count = n

    def __call__(self, func):
        def wrapper (*args, **kwargs):
            print("*" * self.count)
            func(*args, **kwargs)
            print("*" * self.count)
        return wrapper


#аналогічно
@MyDrcorator(15)
def f1(x):
    print(f"Call f1 = {x**2}")

f1(3)


from math import sin, pi
class Derivate:
    def __init__(self, func):
        self._func = func

    def __call__(self, x):
        dx = 1e-5
        result = (self._func(x + dx) - self._func(x))/dx
        return result

@Derivate
def my_sin(x):
    return round(sin(x), 2)

print(my_sin(pi/2))


#                           декоратор методу у класі
def my_decorated(func): # декоратор для методу у класі Test
    def wrapper(self):
        print("*" * 10)
        func(self)
        print("*" * 10)

    return wrapper


class Test:

    def __init__(self, name):
        self.name = name

    @my_decorated
    def info(self):
        print(f"info: {self.name}")


t = Test("init")
t.info()

from functools import wraps

def singleton(orig_cls):
    orig_new = orig_cls.__new__
    instance = None

    def __new__(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = orig_new(cls, *args, **kwargs)
        return instance
    orig_cls.__new__ = __new__
    return orig_cls

@singleton
class Logger:
    def log(msg):
        print(msg)

Logger = singleton(Logger)
logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)