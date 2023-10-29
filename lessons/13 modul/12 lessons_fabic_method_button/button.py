# from abc import ABC, abstractmethod
#
#
# class Button(ABC):
#
#     @abstractmethod
#     def render(self):
#         pass
#
#     @abstractmethod
#     def onclick(self):
#         pass
#
#
# class WindowsButton(Button):
#
#     def render(self):
#         print("Відобразити кнопку в стилі Windows")
#
#     def onclick(self):
#         print('Кнопка Windows була натиснута')
#
#
# class HTMLButton(Button):
#
#     def render(self):
#         print("Повернути HTML-код кнопки")
#
#     def onclick(self):
#         print('Навісити на кнопку обробник події браузера')
#
#
# class Dialog(ABC):
#     def render_dialog(self):
#         button = self.createButton()  # створити кноку
#         button.render()
#         button.onclick()
#
#     @abstractmethod
#     def createButton(self) -> Button:
#         pass
#
#
# class WindowsDialog(Dialog):
#
#     def createButton(self):
#         print("Створено кнопку Windows")
#         return WindowsButton()
#
#
# class WebDialog(Dialog):
#
#     def createButton(self):
#         print("Створено кнопку HTML")
#         return HTMLButton()
#
#
# # if __name__ == "__main__":
# #     wd = WindowsDialog()    # створюємо Windows-діалог
# #     wd.render_dialog()
# #     print()
# #     hd = WebDialog()    # створюємо HTML-діалог
# #     hd.render_dialog()
#
#
# def client_code(creator: Dialog) -> None:
#     print("__Start__")
#     creator.render_dialog()
#
#
# if __name__ == "__main__":
#     client_code(WindowsDialog())
#     client_code(WebDialog())


                          Клон

from copy import copy, deepcopy

class Adress:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def __str__(self):
        return f"вулиця - {self.street}, місто - {self.city}"


class Person:
    def __init__(self, name: str, address: Adress):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Персона {self.name}, живе за адресою: {self.address}"

    def clone(self, name=""):
        name = name if name is not None else self.name
        address = deepcopy(self.address)
        return self.__class__(name, address)


# address = Adress('123 Road', 'London')
# john = Person('John', address)
# print(john) #Персона John, живе за адресою: вулиця - 123 Road, місто - London

# jane = Person('Jain', address)
# print(jane) #Персона Jain, живе за адресою: вулиця - 123 Road, місто - London
# print('_____')
# john.address.street = "100 Road"
# print(john) #Персона John, живе за адресою: вулиця - 100 Road, місто - London
# print(jane) #Персона Jain, живе за адресою: вулиця - 100 Road, місто - London

# #Робимо копію
# address = Adress('123 Road', 'London')
# john = Person('John', address)
# print(john)
#
# jain = deepcopy(john)
# jain.address.street = "100 Road"
# jain.name = "jain"
# print(jain)
# print(john)


#Робимо копію
address = Adress('123 Road', 'London')
john = Person('John', address)
print(john)
print("______")


jain = john.clone(name = "jain")
jain.address.street = "100 Road"

print(jain)
print(john)

#                           Singelton одинак
class Singelton:
    _instance = None # єкземпляр

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.do_work(cls._instance)
        return cls._instance

    def do_work(self):
        print('Init connect to Database')

sing = Singelton()
sing2 = Singelton()
print(sing is sing2)
