# class UserNameDescriptor:
#
#     def __get__(self, instance, owner): #видае результат
#         return getattr(instance, self.var)
#         # return instance.__dict__[self.var] #аналогічний виклик
#
#     def __set__(self, instance, value): #робить присвоення
#         setattr(instance, self.var, value)
#         # instance.__dict__[self.var] = value #аналогічне присвоення
#
#     def __set_name__(self, owner, name): #відповідае за призначення імя атрибута
#         print("Call")
#         var_name =  "_"+ name
#         self.var = var_name
#
#
# class User:
#     username = UserNameDescriptor()
#     name = UserNameDescriptor()
#     last_name = UserNameDescriptor()
#
#     def __init__(self, username, name, last_name):
#         self.username = username #реалізація з дескриптором
#         self.name = name
#         self.last_name = last_name
#
#
# u = User("Admin", "Jon" , "Savchenko")
# print(u.__dict__)
# print(u._username)
#

# class NameDescriptor:
#
#     def __init__(self, prefix="_", lenght = 5): #можна встановити кількість префіксів
#         self.prefix = prefix
#         self.lenght = lenght
#
#     def __set_name__(self, owner, name):  # відповідае за призначення імя атрибута
#         var_name = self.prefix + name
#         self.var = var_name
#
#     def __set__(self, instance, value):  # робить присвоення
#         if len(value) >= self.lenght:
#             setattr(instance, self.var, value)
#         else:
#             raise ValueError
#
#     def __get__(self, instance, owner):  # видае результат
#         return getattr(instance, self.var)
#
# class User:
#     username = NameDescriptor(prefix="__", lenght=5) #встановлюемо кількість префіксів і кількість символів
#     name = NameDescriptor(prefix="__", lenght=2)
#     last_name = NameDescriptor(prefix="__", lenght=5)
#
#     def __init__(self, username, name, last_name):
#         self.username = username  # реалізація з дескриптором
#         self.name = name
#         self.last_name = last_name
#
#
# u = User("Admin", "Jon", "Savchenko")
# print(u.__dict__)



#                                   слот
from sys import getsizeof


class User:
    __slots__ = ("username", "name", "last_name")  # скисок атрибутів які можна визначати, інші неможна, при визначені __slots__ атрибути небудуть додаватися у _dict__

    def __init__(self, username, name, last_name):
        self.username = username  # реалізація з дескриптором
        self.name = name
        self.last_name = last_name


u = User("Admin", "Jon", "Savchenko")
print(u.username, u.name, u.last_name)
size_u = getsizeof(u) #+ getsizeof(u.__dict__)
print(size_u)
