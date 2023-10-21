# Даний клас Student, що описаний як
#
# class Student:
#     team = "Python31"
#     __slots__ = ['name', 'age', 'gender']
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def greet(self):
#         print("Hi, my name is", self.name)
#
#     def description(self):
#         print(f"Person<{self.name}, {self.age}, {self.gender}>")
#
# побудуйте динамічно за допомогою метакласу type() з трьома аргументами.
# Протестуйте роботу.


def custom_init(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

def custom_greet(self):
    print("Hi, my name is", self.name)

def custom_description(self):
    print(f"Person<{self.name}, {self.age}, {self.gender}>")

Student = type('Student', (object,), {
    'team': "Python31",
    '__slots__': ['name', 'age', 'gender'],
    '__init__': custom_init,
    'greet': custom_greet,
    'description': custom_description
})

# Перевірка
student = Student("John", 25, "Male")
student.greet()  # Виведе "Hi, my name is John"
student.description()  # Виведе "Person<John, 25, Male>"



