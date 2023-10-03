class Book:

    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, item):
        print(f"Call __getattr__ {item}")
        if item not in self._attributes:
            raise AttributeError(f'Атрибута {item} немає у викликаемому обекті')
        return self._attributes[item]

    def __setattr__(self, key, value):
        print(f"Call __setattr__ with {key=} {value=}")
        if key == "_attributes":
            super().__setattr__(key, value)
        else:
            self._attributes[key] = value

    def __delattr__(self, item):
        if item not in self._attributes:
            raise AttributeError(f'Атрибута {item} немає у вказаному обєкті')
        else:
            del self._attributes[item]

    def __getattribute__(self, item):
        print(f"Call __getattribute__ with {item}")
        if item in ("_attributes", "__dict__"):
            return super().__getattribute__(item)
        else:
            raise AttributeError("Доступ до неіснуючого атрибуту заборонено")
        return object.__getattribute__(self, item)

#
# # # test __getattribute__
# # print("1_____________________")
# # book = Book("Python Programming", "Ivan Svchenko")
# # print("2_____________________")
# # book.year = 2023
# # print("3_____________________")
# # print(book.__dict__)
# # print("4_____________________")
# # print("book.year = ", book.year)
#
# # # __delattr__
# # book.year = 2023
# # print(book.__dict__)
# # del book.year
# # print(book.__dict__)
#
# # # test __setattr__
# # book.year = 2016
# # print(book.__dict__)
# # print("book.year = ", book.year)
#
# # # test __getattr__
# # print(book.__dict__)
# # print('___________')
# # print("book.title = ", book.title)
# # print("book.author = ", book.author)
# # print("book.year = ", book.year)
#
# # # test __init__
# # print(book.__dict__)
# # print(book.title, book.author)


# Завдання 2.
# Задайте клас Dynamic із приватним атрибутом __attributes, який при ініціалізації є порожнім словником.


class Dynamic:
    def __init__(self):
        self.__attributes = {}

    def __setattr__(self, key, value):
        if key == "_Dynamic__attributes":
            super().__setattr__(key, value)
        else:
            self.__attributes[key] = value

    def __getattr__(self, item):
        if item not in self._Dynamic__attributes:
            raise AttributeError(f'Атрибута {item} немає у викликаемому обекті')
        return self._Dynamic__attributes[item]

    def __delattr__(self, item):
        if item not in self._Dynamic__attributes:
            raise AttributeError(f'Атрибута {item} немає у викликаемому обекті')
        else:
            del self._Dynamic__attributes[item]

    def __getattribute__(self, item):
        if item == "year":
            raise AttributeError (f"Доступ до атрибута {item} заборонено")
        return object.__getattribute__(self, item)


a1 = Dynamic()
a2 = Dynamic()

# # test __getattribute__
# a1.name = 'Ivan'
# a1.year = 2023
# print(a1.__dict__)  # Дозволено
# print(a1.name)  # Дозволено
# print(a1.year)  # Заборонено, викине AttributeError


# # test __setattr__
# print(a1.__dict__)
# print(a2.__dict__)
# a1.name = 'Ivan'
# a2.name = 'Ludmila'
# print(a1.__dict__)
# print(a2.__dict__)

# # test __delattr__
# a1.year = 2023
# print(a1.year)
# print(a1._Dynamic__attributes)
# del a1.year
# print(a1._Dynamic__attributes)

# # test __getattr__
# print(a1.name)
# print(a1.year)


