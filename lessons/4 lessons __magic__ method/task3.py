class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def __str__(self):
        return f"Str: {self.name} - {self.scores}"

    def __repr__(self):
        return f"Repr: {self.name} - {self.scores}"

    def __getitem__(self, item): #повертае індекс
        return self.scores[item]

    def __setitem__(self, key, value):  # key- index
        self.scores[key] = value

    def __delitem__(self, key): #видалення по індексу
        print(f'виконуеться видалення по індексу {key}')
        del self.scores[key]

    def __call__(self, semestr): #обект стае функтором, його можно визивати як функцію
        print(f"Виклик на сесію {semestr}")

    def __getattr__(self, item): #якщо у обекта нема викликаемого атрибута, повертаеться None, якщо його невизначити повертаеться помилак
        print('get attribute')

    def __getattribute__(self, item): #якщо у обекта нема викликаемого атрибута, повертаеться None, якщо його невизначити повертаеться помилак
        print('get attribute name')
        if item == 'name':
            return self.name

A = Student('Alisa', [5, 6, 8, 12])
# print(A.__repr__()) #Repr: Alisa - [5, 6, 8, 12]
# print(repr(A))#Repr: Alisa - [5, 6, 8, 12]
# print(A) # Str: Alisa - [5, 6, 8, 12]

# print(A.scores[-1]) #звернення до останньої оцінки
# print(A[0]) #за рахунок _getitem__ пожно викликати індекс на обекті
# print(*A) # повертае всі єлементи списку
#
# A.scores[0] = 12 #зміна єлементи списку
# A[0] = 10 #за рахунок __setitem__можно змінити за індексом на обекті
#
# del A[0] #за рахунок __delitem__ можно видалити за індексом на обекті
#
# A() # помилка 'Student' object is not callable'      обект невиликаемий
# A() # метод __call__ дозволить виликати обект

print(A.age) #__getattr__повертае None замість помилки
print()




