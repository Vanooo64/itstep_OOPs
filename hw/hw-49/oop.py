class Person:
    '''Клас для створення обэктів з інформацією про імя користувача і данними про його поточний рахунок'''

    def __init__(self, name='xxx', money=0):
        self.name = name
        self.money = money
        self.familiar = []
        print('A new Person is born! ->', self.name)

    def know(self, person):
        if person in self.familiar:
            print(f'{person} вже присутній у списку друзів')
        else:
            self.familiar.append(person)

    def is_known(self, person):
        if person in self.familiar:
            print(f'{self.name} знайомий з {person}')
        else:
            print(f'{self.name} незнайомий з {person}')

    def __str__(self):
        return self.name + str(self.money)

    def giveMoney(self, delta):
        self.money += delta
        print('Захунок {} поповнено на суму {}, всього = {}'.format(self.name, delta, self.money))


A = Person()
B = Person()
C = Person('Petro', 10)
D = Person('Ira', 30)

print('A: Name = {}, money = {:.2f}'.format(A.name, A.money))
print('B: Name = {}, money = {:.2f}'.format(B.name, B.money))

A.name = 'Ivan'
B.name = 'Anna'
B.money = 100.2852

A.giveMoney(50.127)
B.giveMoney(40)

print('A: Name = {}, money = {:.2f}'.format(A.name, A.money))
print('B: Name = {}, money = {:.2f}'.format(B.name, B.money))


def info(person):
    i = person.name + str(person.money)
    return i


print(help(Person))
print(Person.__doc__)

people = [A, B, C, D]

for p in people:
    if p.money < 50:
        p.money += 100

for i in people:
    print(f'{i.name}: Name = {i.name}, money = {i.money}')

A.know('Ivan Savchenko')
A.know('Ludmila')
A.know('Ludmila')
print(A.familiar)
B.is_known('Ludmila')
