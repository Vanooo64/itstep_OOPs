# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# class Baby(Person):
#     def speak(self):
#         print(f"{self.first_name} каже: bla bla bla ")
#
# class Abdult(Person):
#     def speak(self):
#         print(f"My name is {self.first_name}")
#
#
# p1 = Person('Jon', 'Savchenko')
# b1 = Baby('Eva', 'Savchenko')
# a1 = Abdult('Ludmila', 'Madaminova')
# print(p1, isinstance(p1, Person)) # перевіряе чи заданий обект належить цьому класу
# print(b1,  isinstance(b1, Person))
# b1.speak()
# a1.speak()



# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"<{self.first_name} {self.last_name}>"
#
#
# class Baby(Person):
#     def speak(self):
#         print(f"{self.first_name} каже: bla bla bla ")
#
# class Abdult(Person):
#     def speak(self):
#         print(f"My name is {self.first_name}")
# class BatterPerson(Person):
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
# p1 = BatterPerson('Jon', 'Savchenko')
# p1.first_name = 'Jon2'
# print(p1.full_name)



#                   super() клас

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"<{self.first_name} {self.last_name}>"
#
# class Student(Person):
#     def __init__(self, first_name, last_name, school): # порушуется принцип dry
#         self.first_name = first_name
#         self.last_name = last_name
#         self.school = school
#
# s = Student ('jon', 'Savchenko', '№3')
# print(s)

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"<{self.first_name} {self.last_name}>"
#
# class Student(Person):
#     def __init__(self, first_name, last_name, school):      # додавання атрибуту обекту до батьківського класу
#         super().__init__(first_name, last_name)             # super() - проксі обект надае доступ до класу Person
#         self.school = school
#
#     def __str__(self):
#         return f"<{self.first_name}, {self.last_name}, {self.school}>"
#
# s = Student ('jon', 'Savchenko', '№3')
# print(s)


# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"<{self.first_name} {self.last_name}>"
#
#     def print_info(self):
#         print(f"{self.first_name[0]}. {self.last_name}", end=' ')
#
# class Test:
#     def info(self):
#         print(f'test !!!! {self.__class__.__name__}') # повертае імя класу з якого був створенний обект
#
# class Student(Person, Test): # множинне наслідування
#     def __init__(self, *args, school):      # візьме всі аргумети батьківського класу
#         super().__init__(*args)             # super() - проксі обект надае доступ до класу Person
#         self.school = school
#
#     def __str__(self):
#         return f"<{self.first_name}, {self.last_name}, {self.school}>"
#
#     def print_info(self):
#         super().info()          # унаслідеу метод із класу Test
#         super().print_info()    # унаслідуе функцонал print_info класу Person
#         print(self.school)      # модифікуемо існуючий метод
#
# s = Student ('Jon', 'Savchenko', school='№3')
# print(s)
# s.print_info()
#
# print(Student.__mro__) #показуе рівні наслідування (<class '__main__.Student'>, <class '__main__.Person'>, <class '__main__.Test'>, <class 'object'>)
#
# mro = [x.__name__ for x in Student.__mro__]
# print(mro) #показуе рівні наслідування ['Student', 'Person', 'Test', 'object']


# class Dog:
#     def make_sound(self):
#         print('Woof!')
#
# class Cat:
#     def make_sound(self):
#         print('Miaw!')
#
#
# d= Dog()
# c = Cat()
# d.make_sound()
# c.make_sound()
#
# def get_sound(x):
#     x.make_sound()
#
# print()
# get_sound(d)
# get_sound(c)







# class Money:
#     def __init__(self, amount, currency):
#         self.amount = amount
#         self.currency = currency
#
#     def __str__(self):
#         return f"{self.amount} {self.currency}"
#
#
# class BankAccount:
#     accounts = []
#     __exchange_rate = {}
#
#     def __init__(self, account_number, balance, owner_name, currency):
#         self.__account_number = account_number
#         self.balance = Money(balance, currency)
#         self.owner_name = owner_name
#         self.accounts.append(self)  # додає  у список всі створені об'єкти
#
#     @classmethod
#     def create_exchange_rate(cls):
#
#
#         # prepare data from API
#         cls.__exchange_rate =  # data from API
#
#     def transfer(self, recipient_account, money):
#         """
#         Переказує гроші з поточного рахунку на рахунок отримувача.
#
#         Параметри:
#         recipient_account (BankAccount): Рахунок отримувача.
#         money (Money): Сума грошей та валюта для переказу.
#
#         Повертає:
#         None
#         """
#         if self.balance.currency != money.currency:
#             print("Неможливо здійснити переказ між рахунками з різними валютами.")
#             return
#
#         if money.amount < 0:
#             print("Сума переказу не може бути від'ємною!")
#
#         if money.amount <= self.balance.amount:
#             self.withdraw(money.amount)
#             recipient_account.deposit(money.amount)
#             print("Переказ здійснено успішно")
#         else:
#             print(f"На рахунку {self.owner_name} недостатньо коштів, поточний баланс = {self.balance.amount}")
#
#     def deposit(self, amount):
#         self.balance.amount += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance.amount:
#             self.balance.amount -= amount
#         else:
#             print("На рахунку недостатньо коштів")
#
#     def __str__(self):
#         return f"Bank Account - {self.__account_number}, Balance - {self.balance.amount}, Owner - {self.owner_name}, Currency - {self.balance.currency}"
#
#
# # # Створення об'єктів BankAccount
# # account1 = BankAccount(10000, 100, 'Ivan Sacvhenko', 'USD')
# # account2 = BankAccount(20000, 100, 'Madaminova Ludmila', 'EUR')
# # account3 = BankAccount(30000, 100, 'Voloschin Oleksandr', 'UAH')
# # account4 = BankAccount(40000, 200, 'Ivan Sacvhenko', 'UAH')
# # account5 = BankAccount(50000, 175, 'Ivan Sacvhenko', 'USD')
# #
# # # Переказ коштів між рахунками
# # account1.transfer(account5, Money(10, "USD"))
# # print("Після переказу:")
# # print(account1)
# # print(account5)
# #
# # # Ще один переказ коштів між рахунками
# # account2.transfer(account3, Money(50, "USD"))
# # print("Після ще одного переказу:")
# # print(account2)
# # print(account3)





