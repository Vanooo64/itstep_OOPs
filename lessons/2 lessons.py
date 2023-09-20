# class Person: #пустий клас
#     pass
#
# class Person: # аналогычно
#     ...

# class MyClass:
#     rate = '123'
#
#     def __init__(self, x):
#         self.x = x
#
#     def get_type(self, n): #статтичний метод, коли в тілі функції невикористовуеться self
#         res = MyClass.rate * n
#         print(res)
#
# obj = MyClass(5)
# MyClass.get_type(5)
# obj.get_type(3)

# class MyClass:
#     rate = '123'
#
#     def __init__(self, x):
#         self.x = x
#
#     @staticmethod
#     def get_type(n): #статтичний метод, коли в тілі функції невикористовуеться self
#         res = MyClass.rate * n
#         print(res)
#
# obj = MyClass(5)
# MyClass.get_type(5)
# obj.get_type(3)


# class MyClass:
#     rate = '123'
#
#     def __init__(self, x):
#         self.x = x
#
#     @staticmethod
#     def get_type(n): #статтичний метод, коли в тілі функції невикористовуеться self
#         res = MyClass.rate * n
#         print(res)
#     def get_type_2(self, n): #статтичний метод, коли в тілі функції невикористовуеться self
#         res = type(self).rate * n
#         print(res)
#
# obj = MyClass(5)
# MyClass.get_type(5)
# obj.get_type_2(4)
# print(type(obj))
# print(obj.__dict__) #повертае атрибути обекту
# print(MyClass.__module__) #повертаэ main якщо ми запускаемо програму у поточному файлы, Якщо запускаемо з ыншого файлу повертае назву файлу
# print(vars(MyClass)) #повертае атрибути обекту
# obj.__dict__['color'] = 'black' #додае атрибут в обект
# # obj.color = 'black' # аналогічно
# print(obj.__dict__)
# print(hasattr(obj, 'color')) #вертае True якщо є такий атрибут
# print(hasattr(obj, 'age'))
# setattr(obj,'age', 3) #додавання атрибуту
# print(obj.__dict__)
# delattr(obj,'age') #видалення атрибуту


#                           classmethod
# class MyClass:
#     rate = '123'
#
#     def __init__(self, x):
#         self.x = x
#
#     @staticmethod
#     def get_type(n):  # статтичний метод, коли в тілі функції невикористовуеться self
#         res = MyClass.rate * n
#         print(res)
#
#     def get_type_2(self, n):  # статтичний метод, коли в тілі функції невикористовуеться self
#         res = type(self).rate * n
#         print(res)
#
#     @classmethod
#     def get_type_3(cls, n):  # передаемо клас
#         res = cls.rate * n
#         print(res)
#
#
# obj = MyClass(5)
# MyClass.get_type_3(10) # == MyClass.get_type_3(MyClass, n)
# obj.get_type_3(10)

# class MyClass:
#     rate = '123'
#
#     def __init__(self, x, age=0):
#         print('Begin int')
#         self.x = x
#         self.age = age
#
#     @classmethod
#     def make(cls, n, year):
#         print(f"before create obj: {n} {year}")
#         cls.new_attr = "attr_class" #додавання атрибуту
#         age = 2023 - year
#         new_obj = cls(n, age) #створення обекта і присвоення нових значень
#         return new_obj
#
# some_obj = MyClass.make(10, 2000) #виклик класметоду
# print(some_obj.__dict__)


# class Person:
#
#     def __new__(cls, name, age): #метод додае якусь логіку до __init__
#         print('Begin magic method __new__') #додаемо логіку
#         return super().__new__(cls) #super() = object повертаемо попередню логіку батькіського класу
#
#     def __init__(self, name, age=0):
#         print('Begin int')
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def make(cls, name, year):
#         print(f"before create obj: {name} {year}")
#         return cls(name, 2023 - year) #створення обекта і присвоення нових значень
#
#
# obj = Person('Jon', 20)
# print(obj) #атрибути обекта


#                       Інкапсуляція

# class Person:
#
#     def __init__(self, name, age=0):
#         print('Begin int')
#         self._name = name #сигналізація що краще метод не чіпати,але це можна робити
#         self.__age = age #захищенний атрибут, який неможна змінювати
#
#     def __str__(self):
#         return f"{self._name} {self.__age}"
#
#
# obj = Person("Jon", 20)
# # print(obj._name, obj.__age)
# print(obj._name, obj._Person__age) #Отримання доступу (достукатись)
# obj._name = 'Eva'
# obj.__age = 10 #створить новий атрибут
# print(vars(obj))
# print(obj)



#                 гетери і сетори
# class Person:
#
#     def __init__(self, name, age=0):
#         print('Begin int')
#         self._name = name  # сигналізація що краще метод не чіпати,але це можна робити
#         self.__age = age  # захищенний атрибут, який неможна змінювати
#
#     def __str__(self):
#         return f"{self._name} {self.__age}"
#
#     def get_age(self): #повертае захищенний атрибу
#         return self.__age
#
#     def set_age(self, age):  # сетер для зміни захищених атрибутів
#         self.__age = age
#
#
# obj = Person("Jon", 20)
# print(obj.get_age())
#
# print(obj) #Jon 20
# obj.set_age(10) #зміна age
# print(obj) #Jon 10

#                       Декоратори геттера і сетора
class Person:

    def __init__(self, name, age=0):
        self._name = name  # сигналізація що краще метод не чіпати,але це можна робити
        self.__age = age  # захищенний атрибут, який неможна змінювати

    def __str__(self):
        return f"{self._name} {self.__age}"

    @property  # декоратор для повернення гетера
    def age(self):  # повертае захищенний атрибу
        return self.__age

    @age.setter
    def age(self, age):  # сетер для зміни захищених атрибутів
        try:
            if age < 0: #перевірка до присвоення
                raise ValueError('Age is not positive')
            self.__age = age # gприсвоення
        except ValueError:
            print('Value is not changed')


obj = Person("Jon", 20)
print(obj)
obj.age = -5
print(obj)
