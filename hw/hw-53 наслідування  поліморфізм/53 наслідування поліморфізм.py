# #                           Домашня робота No53 ООП. Поліформізм. Наслідування.
# # Завдання 1
# # Визначте три класи: Printer, Lamp і Car. Кожен з них має тільки один метод does(). Він повертає значення 'print' (для Printer), 'glow' (для Lamp) або 'ride' (для Car). Далі визначте клас Robot з методом __init__, який містить по одному екземпляру кожного з цих класів як власні атрибути. Визначте метод do_it() для класу Robot, який виводить на екран усі дії, що роблять його компоненти.
# # P.S. Тут наслідування не робити, це завдання на поліморфізм щодо методу does() для різних типів об’єктів.
#
# class Printer:
#     def does(self):
#         return 'print'
#
# class Lamp:
#     def does(self):
#         return 'glow'
#
# class Car:
#     def does(self):
#
#         return 'ride'
#
# class Robot:
#     def __init__(self):
#         self.printer = Printer()
#         self.lamp = Lamp()
#         self. car = Car()
#
#     def do_it(self):
#         print("Robot can", robot.printer.does())  # виведе "Robot can print"
#         print("Robot can", robot.lamp.does())  # виведе "Robot can glow"
#         print("Robot can", robot.car.does())  # виведе "Robot can ride"
#
# # Приклад використання
# robot = Robot()
# robot.do_it()

# # Завдання 2
# # Створіть ієрархію класів для представлення осіб з різними характеристиками, використовуючи клас `Person` як батьківський клас.
# # 1. Створіть клас `Person` з атрибутами `name` і `age`. Реалізуйте метод __init__. Додайте також метод `introduce()`, який виводить ім'я та вік особи.
# # 2. Створіть клас `Student`, який успадковує клас `Person`. Додайте атрибут ` id` при ініціалізації об’єкта (перевизначте метод __init__, в якому буде викликатись за допомогою super батьківський __init__). Додайте метод `study(subject)`, який виводить повідомлення, що студент {self.name}- {self.id} навчається предмету subject.
# # 3. Створіть клас `Teacher`, який успадковує клас `Person`. Додайте атрибут `subject` та метод ` teach(s)`, який виводить повідомлення, що «викладач {self.name} навчає {self.subject} студента {s.name}», де s – це деякий екземпляр Student. У методі teach зробіть перевірку чи s є дійсно об`єктом з класу Student, якщо ні, то вивести відповідне повідомлення.
# # 4. Створіть клас `Employee`, який успадковує клас `Person`. Додайте атрибути salary, specialty та метод `work()`, який виводить повідомлення про роботу співробітника та його зарплату.
# # 5. Створіть по одному об'єкту кожного з класів `Student`, `Teacher`, `Employee` і викличте методи, що відповідають їхній ролі. Протестуйте роботу методів, що задаються у них
# # 7. Перевизначте метод ` introduce()` у класах `Student`, `Teacher`, `Employee`, щоб вони давали всю інформацію про особу та назву класу, до якого вона відноситься. Протестуйте роботу.
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         return f"Особу звати {self.name} її вік {self.age}"
#
#
# class Student(Person):
#     def __init__(self, id, name, age):
#         self.id = id
#         super().__init__(name, age)
#
#     def study(self, subject):
#         return f"Студент {self.name} - {self.id} навчається предмету {subject}"
#
#     def introduce(self):
#         return f"Особу звати {self.name} ID - {self.id} її вік {self.age}"
#
#
# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#
#     def teach(self, s):
#         if isinstance(s, Student):
#             return f"Викладач {self.name} навчає {self.subject} студента {s.name}"
#         else:
#             return "Неприпустимий об'єкт. Очікується об'єкт класу Student."
#
#     def introduce(self):
#         return f"Викладача звати {self.name} його вік {self.age}, викладає {self.subject}"
#
#
# class Employee(Person):
#     def __init__(self, name, age, salary, specialty):
#         super().__init__(name, age)
#         self.salary = salary
#         self.specialty = specialty
#
#     def work(self):
#         return f"Співробітник {self.name} працює {self.specialty} його зарплата {self.salary}"
#
#     def introduce(self):
#         return f"Співробітника звати {self.name} його вік {self.age}, спеціальність {self.specialty}, зарплат {self.salary}"
#
#
# p1 = Person('Ivan', 30)
# print(p1.introduce())
#
# s1 = Student(1, 'Ludmila', 30)
# # print(s1.study('Python'))
#
# t1 = Teacher('Jon', 40, "OOPs")
# # print(t1.teach(s1))
#
# e1 = Employee('Jon', '40', 250000, 'Programer')
# # print(e1.work())
#
# print(s1.introduce())
# print(t1.introduce())
# print(e1.introduce())



#                   task 3
import datetime

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Baby(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def speak(self):
        print('Blah blah blah')


class Adult(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def speak(self):
        print(f'Hello, my name is, {self.first_name}')

class Calendar:
    def book_appointment (self, date):
        print('Booking appointment for date', date)

class OrganizedAdult(Adult, Calendar):
    def __init__(self, first_name, last_name):
        Adult.__init__(self, first_name, last_name)
        Calendar.__init__(self)

class OrganizedBaby(Baby, Calendar):
    def __init__(self, first_name, last_name):
        Baby.__init__(self, first_name, last_name)
        Calendar.__init__(self)

    def book_appointment(self, date):
        print("Note that you are booking an appointment with a baby.")
        super().book_appointment(date)

andres = OrganizedAdult('Andres', 'Gomez')
boris = OrganizedBaby('Boris', 'Bumblebutton')
andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018, 1, 1))