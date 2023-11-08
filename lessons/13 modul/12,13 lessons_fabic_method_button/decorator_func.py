from typing import Callable


def f1():
    print('Call f1')


def f2(f: Callable):
    return f


f1()
f2(f1)()

#декоратор на прикладі функції
from typing import Callable


def decorator(func: Callable):
    print("decor")
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def f1():
    print('Call f1')


f1()

from typing import Callable


def decorator(func: Callable):
    print("decor")
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper

@decorator
def f1(x):
    print(f'Call f1 = {x**2}')


f1(3)


# декорування доступу
permissions = ['user', 'admin']

def required(permission):
    def decorate(func):
        def wrapper(*args, **kwargs):
            if permission in permissions:
                func(*args, **kwargs)
            else:
                raise ValueError(f'Нема доступу для користувача {permission}')

        return wrapper
    return decorate

@required(permission='admin')
def data():
    print('secret data')

data()

