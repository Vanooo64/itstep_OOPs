# # Завдання 1.
# # Реалізувати дескриптор не даних, який повертає довжину імені екземпляра класу Person. Допишіть код та протестуйте його виконання.
#
#
# class Size:
#     def __get__(self, obj, objtype=None):
#         if obj is None:
#             return self
#         return len(obj.name)
# class Person:
#     size_name = Size() # implement Descriptor instance
#     def __init__(self, name):
#         self.name = name # Regular instance attribute
#
#
# person = Person('John Doe')
# print(f"Довжина імені {person.name} = {person.size_name}")  # Повертає довжину імені, наприклад: 8


# Завдання 2.
# Задайте клас User, що має атрибути-дескриптори username і password, які контролюють доступ до відповідних атрибутів _username` та `_password.

class UsernameDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        if not (4 <= len(value) <= 10):
            raise ValueError("Довжина username повинна бути від 4 до 10 символів")
        if not value[0].isalpha():
            raise ValueError("Username не повинен починатись з цифри")
        else:
            instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class PasswordDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        if len(value) >= 8:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Password повинен містити принаймні 8 символів.")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class User:
    username = UsernameDescriptor()
    password = PasswordDescriptor()

    def __init__(self, username, password):
        self.username = username
        self.password = password


u1 = User("Vano1", "Vds33433")
print(u1.__dict__)


