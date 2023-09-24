class BankAccount:

    def __init__(self, account_number, balance, owner_name):
        self.__account_number = account_number
        self._balance = balance
        self.owner_name = owner_name

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

    def __str__(self):
        return (f'Клас - {BankAccount.__name__}, номер рахунку - {self.account_number}, баланс - {self.balance}''')

    @staticmethod
    def check_account_number(account_number):
        """
        Перевіряє, чи є вказаний номер рахунку валідним (складається рівно з 5 цифр).

        Параметри:
        account_number (int): Номер рахунку для перевірки.

        Повертає:
        bool: True, якщо номер рахунку валідний; False, якщо невалідний.
        """
        return len(str(account_number)) == 5 and str(account_number).isdigit()


    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("На рахунку недостатньо коштів")

    def transfer(self, recipient_account, money):
        """
        Переказує гроші з поточного рахунку на рахунок отримувача.

        Параметри:
        recipient_account (BankAccount): Рахунок отримувача.
        money (float): Сума грошей для переказу.

        Повертає:
        None
        """
        if money < 0:
            print("Сума переказу не може бути від'ємною!")

        if money <= self.balance:
            self.withdraw(money)
            recipient_account.deposit(money)
            print("Переказ здійснено успішно")
        else:
            print(f"На рахунку {self.owner_name} недостатьно коштів, поточний рахунок = {self.balance}")

    def change_owner_name(self, new_name):
        self.owner_name = new_name

    def display_account_info(self):
        return (f'''Клас - {BankAccount.__name__}, номер рахунку - {self.account_number}, баланс - {self.balance}, імя власника - {self.owner_name}''')


acaunt1 = BankAccount(10000,100, 'Ivan Sacvhenko' )
acaunt2 = BankAccount(20000, 100, 'Madaminova Ludmila')


# Приклад використання
account_number1 = 12345
account_number2 = 123456

print("Чи дійсний рахунок № 1?", BankAccount.check_account_number(account_number1))  # True
print("Чи дійсний рахунок № 2?", BankAccount.check_account_number(account_number2))  # False
print("Чи дійсний рахунок № 1?", acaunt1.check_account_number(account_number1))  # True
print("Чи дійсний рахунок № 2?", acaunt2.check_account_number(account_number2))  # False

print(f"Результат сеттеру для обекта acaunt1 = {acaunt1.account_number}")
acaunt1.account_number = 30000 #використання сетеру
print(acaunt1.account_number)

