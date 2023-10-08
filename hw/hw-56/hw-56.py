from NewBank import NewBankAccount


class UpBankAccount(NewBankAccount):

    def __eq__(self, other):
        """Прирывнюэ об'єкти за їхніми значеннями =="""
        if self.balance.currency == other.balance.currency:
            return True
        return False

    def __lt__(self, other):
        """Порівнюємо об'єкти за їхніми значеннями <"""
        return self.balance < other.balance

    def __le__(self, other):
        """Порівнюємо об'єкти за їхніми значеннями <="""
        return self.balance <= other.balance

    def __gt__(self, other):
        """Порівнюємо об'єкти за їхніми значеннями >"""
        return self.balance > other.balance

    def __ge__(self, other):
        """Порівнюємо об'єкти за їхніми значеннями >="""
        return self.balance >= other.balance

    def __bool__(self):
        if self.balance.amount > 0:
            return True
        return False

    def __add__(self, other):
        if other < 0:
            raise ValueError("Для операції додавання очікується додатне число.")
        self.balance.amount += other
        return self

    def __sub__(self, other):
        if other < 0:
            raise ValueError("Для операції віднімання очікується додатне число.")
        if self.balance.amount < other:
            raise ValueError("На рахунку недостатьно коштів")
        self.balance.amount -= other
        return self

    def __call__(self, value=0):
        if value < 0:
            self.balance.amount += value
            return self
            print(f"Баланс рахунку зменшено на {value} одиниць, його сума = {self.balance.amount} ")

        if value > 0:
            self.balance.amount += value
            return self
            print(f"Баланс рахунку збільшився на {value} одиниць, його сума = {self.balance.amount} ")

        if value == 0:
            print(f"Баланс рахунку збільшився {self.balance.amount} ")

    def __setattr__(self, name, value):
        if name == 'balance':
            self.__dict__[name] = value
            print(f"Зміна балансу: було {self.balance}, стало {value.amount}")


if __name__ == "__main__":
    account8 = UpBankAccount(80000, 1000, "Ivan Savcenko", "UAH", 500, 10)
    account9 = UpBankAccount(90000, 10000, "Madaminova Ludmila", "UAH", 500, 10)

    account8.balance = 90000
    print(account8)


    # # перевырка методу __call__
    # print(account8.__call__(-150))

    # # перевырка методу __sub__
    # print(account8 - 500)

    # # перевырка методу __add__
    # print(account8 + 500)

    # # перевырка методу __bool__
    # print(account8.__bool__())

    # # перевырка методу __gе__ >=
    # print(account9 >= account8)

    # # перевырка методу __ge__ >
    # print(account9 >= account8)

    # # перевырка методу __le__ <=
    # print(account9 <= account8)

    # # перевырка методу __lt__ <
    # print(account9 < account8)

    # перевырка методу __eq__
    # print(f"Валюта акунта №{account8.account_number} дорівнює валюті акаунта №{account9.account_number}: {account9 == account8}")

# if self.balance.currency == other.balance.currency:
#     raise ValueError("Неможливо порівняти рахунки з різними валютами.")