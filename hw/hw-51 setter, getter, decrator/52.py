import requests
import json

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"


class BankAccount:
    accounts = []
    __exchange_rate = {} #{'AUD': 23.4844, 'CAD': 27.1623...}

    def __init__(self, account_number, balance, owner_name, currency):
        self.__account_number = account_number
        self.balance = Money(balance, currency)
        self.owner_name = owner_name
        BankAccount.accounts.append(self)  # додає  у список всі створені об'єкти

    @classmethod
    def create_exchange_rate(cls):
        responce = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
        json_text = responce.text
        data = json.loads(json_text)
        cls.__exchange_rate = {currency['cc']: currency['rate'] for currency in data}

    def transfer_funds(self, target_account, amount):


    def transfer(self, recipient_account, money):
        """
        Переказує гроші з поточного рахунку на рахунок отримувача.

        Параметри:
        recipient_account (BankAccount): Рахунок отримувача.
        money (Money): Сума грошей та валюта для переказу.

        Повертає:
        None
        """
        if self.balance.currency != money.currency:
            print("Неможливо здійснити переказ між рахунками з різними валютами.")
            return

        if money.amount < 0:
            print("Сума переказу не може бути від'ємною!")

        if money.amount <= self.balance.amount:
            self.withdraw(money.amount)
            recipient_account.deposit(money.amount)
            print("Переказ здійснено успішно")
        else:
            print(f"На рахунку {self.owner_name} недостатньо коштів, поточний баланс = {self.balance.amount}")

    def deposit(self, amount):
        self.balance.amount += amount

    def withdraw(self, amount):
        if amount <= self.balance.amount:
            self.balance.amount -= amount
        else:
            print("На рахунку недостатньо коштів")

    def __str__(self):
        return f"Bank Account - {self.__account_number}, Balance - {self.balance.amount}, Owner - {self.owner_name}, Currency - {self.balance.currency}"

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

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

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        """
        Пошук рахунків за власником.

        Параметри:
        owner_name (str): Ім'я власника.

        Повертає:
        list: Список об'єктів BankAccount, які належать даному власнику.
        """
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        """
        Отримання середнього балансу коштів у всіх рахунках.

        Повертає:
        float: Середній баланс коштів.
        """
        total_balance = sum(account.balance.amount for account in cls.accounts)
        return total_balance / len(cls.accounts)

    def change_owner_name(self, new_name):
        self.owner_name = new_name

    def display_account_info(self):
        """
        Повертає рядок з інформацією про рахунок.

        Повертає:
        str: Рядок з інформацією про рахунок.
        """
        return f"Клас - {BankAccount.__name__}, номер рахунку - {self.account_number}, баланс - {self.balance.amount}, ім'я власника - {self.owner_name}"

BankAccount.create_exchange_rate()
print(BankAccount._BankAccount__exchange_rate)
# # Створення об'єктів BankAccount
# account1 = BankAccount(10000, 100, 'Ivan Sacvhenko', 'USD')
# account2 = BankAccount(20000, 100, 'Madaminova Ludmila', 'EUR')
# account3 = BankAccount(30000, 100, 'Voloschin Oleksandr', 'UAH')
# account4 = BankAccount(40000, 200, 'Ivan Sacvhenko', 'UAH')
# account5 = BankAccount(50000, 175, 'Ivan Sacvhenko', 'USD')
#
# # Переказ коштів між рахунками
# account1.transfer(account5, Money(10, "USD"))
# print("Після переказу:")
# print(account1)
# print(account5)
#
# # Ще один переказ коштів між рахунками
# account3.transfer(account4, Money(50, "USD"))
# print("Після ще одного переказу:")
# print(account3)
# print(account4)
#
# # # Показ середнього балансу
# # print(f"Середній баланс коштів всіх об'єктів 'BankAccount': {BankAccount.get_average_balance()}")