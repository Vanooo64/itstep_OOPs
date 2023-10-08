import requests
import json
import os


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __lt__(self, other):
        # Порівнюємо об'єкти за їхніми значеннями <
        if self.currency == other.currency:
            return self.amount < other.amount
        else:
            raise ValueError("Неможливо порівняти Money об'єкти з різними валютами.")

    def __le__(self, other):
        # Порівнюємо об'єкти за їхніми значеннями <=
        if self.currency == other.currency:
            return self.amount <= other.amount
        else:
            raise ValueError("Неможливо порівняти Money об'єкти з різними валютами.")

    def __gt__(self, other):
        # Порівнюємо об'єкти за їхніми значеннями >
        if self.currency == other.currency:
            return self.amount > other.amount
        else:
            raise ValueError("Неможливо порівняти Money об'єкти з різними валютами.")

    def __ge__(self, other):
        # Порівнюємо об'єкти за їхніми значеннями >
        if self.currency == other.currency:
            return self.amount >= other.amount
        else:
            raise ValueError("Неможливо порівняти Money об'єкти з різними валютами.")


class BankAccount:
    accounts = []
    __exchange_rate = {}  # return {'AUD': 23.4844, 'CAD': 27.1623...}
    data_folder = os.path.dirname(
        os.path.realpath(__file__))  # посилання на папку в якому знаходиться файл який виконуеться

    def __init__(self, account_number, balance, owner_name, currency):
        self.__account_number = account_number
        self.balance = Money(balance, currency)
        self.owner_name = owner_name
        BankAccount.accounts.append(self)  # додає  у список всі створені об'єкти
        self.file_path = os.path.join(BankAccount.data_folder,
                                      f"{account_number}.txt")  # Створення файла для збереження інформації про рахунок
        self.save_to_file()

    def save_to_file(self):
        """
        Зберігає інформацію про рахунок у вигляді текстового файлу.
        """
        account_info = {
            "account_number": self.__account_number,
            "balance": self.balance.amount,
            "owner_name": self.owner_name,
            "currency": self.balance.currency
        }

        with open(self.file_path, 'w') as file:
            json.dump(account_info, file)

    @classmethod
    def load_from_file(cls, account_number):
        """
        Завантажити інформацію про обліковий запис із файлу на основі номера рахунку.

        Параметри:
        account_number (int): номер рахунку для завантаження.

        Повернення:
        BankAccount або None: Об’єкт BankAccount, завантажений із файлу, або None, якщо файл не існує.
        """
        file_path = os.path.join(BankAccount.data_folder, f"{account_number}.txt")

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                account_info = json.load(file)
                return cls(account_info["account_number"], account_info["balance"], account_info["owner_name"],
                           account_info["currency"])
        else:
            print(f"Файл для рахунку з номером {account_number} не існує.")
            return None

    @classmethod
    def delete_account(cls, account_number):
        """
        Видаляє банківський рахунок за номером та його файл з папки data.

        Parameters:
        account_number (int): Номер рахунку для видалення.

        Returns:
        bool: True, якщо рахунок та файл успішно видалені; False, якщо не вдалося видалити.
        """
        account = cls.load_from_file(account_number)
        if account:
            file_path = os.path.join(BankAccount.data_folder, f"{account_number}.txt")

            try:
                # Видаляємо файл
                os.remove(file_path)
            except OSError as e:
                print(f"Помилка при видаленні файлу: {str(e)}")
                return False

            # Видаляємо об'єкт рахунку зі списку
            cls.accounts.remove(account)
            print(f"Рахунок з номером {account_number} та відповідний файл успішно видалені.")
            return True
        else:
            print(f"Рахунок з номером {account_number} не існує.")
            return False

    @classmethod  # підтягуе курси валют з API НБУ
    def create_exchange_rate(cls):
        responce = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
        json_text = responce.text
        data = json.loads(json_text)
        cls.__exchange_rate = {currency['cc']: currency['rate'] for currency in data}

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
            return False

        if money.amount < 0:
            print("Сума переказу не може бути від'ємною!")

        if money.amount <= self.balance.amount:
            self.withdraw(money.amount)
            recipient_account.deposit(money.amount)
            print("Переказ здійснено успішно")
            return True
        else:
            print(f"На рахунку {self.owner_name} недостатньо коштів, поточний баланс = {self.balance.amount}")

    def deposit(self, amount):
        self.balance.amount += amount

    def withdraw(self, amount):
        if amount <= self.balance.amount:
            self.balance.amount -= amount
        else:
            print("На рахунку недостатньо коштів")

    def transfer_funds(self, target_account, amount):
        """
        Переказує кошти між рахунками, при необхідності враховуючи курс валют.

        Параметри:
        target_account (BankAccount): рахунок одержувача..
        amount (float): сума грошей для переказу.

        Повернення:
        bool: True, якщо передача була успішною, False в іншому випадку.
        """
        if self.balance.currency != target_account.balance.currency:
            if self.balance.currency in BankAccount.__exchange_rate and target_account.balance.currency in BankAccount.__exchange_rate:
                # Convert to a common currency (UAH) using the exchange rates
                common_currency_amount = amount / BankAccount.__exchange_rate[self.balance.currency]
                converted_amount = common_currency_amount * BankAccount.__exchange_rate[
                    target_account.balance.currency]

                if self.balance.amount >= amount:
                    self.withdraw(amount)
                    target_account.deposit(converted_amount)
                    print("Передача успішно завершена")
                    return True
                else:
                    print("Недостатньо коштів на вихідному рахунку.")
            else:
                print("Курси обміну недоступні для валют.")
        else:
            if self.balance.amount >= amount:
                self.withdraw(amount)
                target_account.deposit(amount)
                print("Передача успішно завершена")
                return True
            else:
                print("Недостатньо коштів на вихідному рахунку.")

        return False

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

if __name__ == "__main__":

    BankAccount.create_exchange_rate()
    print(BankAccount._BankAccount__exchange_rate)
    # Створення об'єктів BankAccount
    account1 = BankAccount(10000, 100, 'Ivan Sacvhenko1', 'USD')
    account2 = BankAccount(20000, 100, 'Madaminova Ludmila', 'EUR')
    account3 = BankAccount(30000, 100, 'Voloschin Oleksandr', 'UAH')
    account4 = BankAccount(40000, 200, 'Ivan Sacvhenko', 'UAH')
    account5 = BankAccount(50000, 175, 'Ivan Sacvhenko', 'USD')
    #
    # # Переказ коштів між рахунками
    # account1.transfer(account5, Money(10, "USD"))
    # print("Після переказу:")
    # print(account1)
    # print(account5)
    # #
    # # Ще один переказ коштів між рахунками
    # account3.transfer(account4, Money(50, "USD"))
    # print("Після ще одного переказу:")
    # print(account3)
    # print(account4)
    # #
    # # Показ середнього балансу
    # print(f"Середній баланс коштів всіх об'єктів 'BankAccount': {BankAccount.get_average_balance()}")

    # print("Before transfer_funds:")
    # print(account1)
    # print(account2)
    #
    # # Transfer from account1 (USD) to account2 (EUR)
    # account1.transfer_funds(account2, 10)
    #
    # print("After transfer_funds:")
    # print(account1)
    # print(account2)
    #
    # # Видалення рахунку та файлу
    # BankAccount.delete_account(50000)

