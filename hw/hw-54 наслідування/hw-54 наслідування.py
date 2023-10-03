from bank import BankAccount, Money


class NewBankAccount(BankAccount):

    def __init__(self, account_number, balance, owner_name, currency, max_limit, max_count_transactions):
        super().__init__(account_number, balance, owner_name, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions

    def __str__(self):
        return f"NewBankAccount - {self._BankAccount__account_number}, Баланс - {self.balance.amount}, Власник- {self.owner_name}, Валюта - {self.balance.currency}, Максимальний ліміт на зняття/переказ коштів  - {self.max_limit}, Максимальна можлива кількість операцій щодо зняття/переказів - {self.max_count_transactions}"

class NewBankAccount(BankAccount):
    def __init__(self, account_number, balance, owner_name, currency, max_limit, max_count_transactions):
        super().__init__(account_number, balance, owner_name, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions

    def withdraw(self, amount):
        if amount > self.max_limit:
            print("Перевищено максимальний ліміт на зняття коштів.")
            return False

        if self.max_count_transactions <= 0:
            print("Досягнуто максимальну кількість операцій зняття/переказу.")
            return False

        if amount <= self.balance.amount:
            self.balance.amount -= amount
            self.max_count_transactions -= 1
            print(f"Зняття {amount} {self.balance.currency}. Залишок: {self.balance.amount}")
            return True
        else:
            print("Недостатньо коштів на рахунку.")
            return False

    def transfer(self, recipient_account, amount):
        if amount > self.max_limit:
            print("Перевищено максимальний ліміт на переказ коштів.")
            return False

        if self.max_count_transactions <= 0:
            print("Досягнуто максимальну кількість операцій зняття/переказу.")
            return False

        if amount <= self.balance.amount:
            self.balance.amount -= amount
            recipient_account.deposit(amount)
            self.max_count_transactions -= 1
            print(f"Переказ {amount} {self.balance.currency} на рахунок {recipient_account.owner_name}.")
            return True
        else:
            print("Недостатньо коштів на рахунку.")
            return False

    def add_percent_balance (self, percent):
        """Додає відсотки до балансу рахунку.

        Параметри:
        percent (float): Відсоток, який потрібно додати до балансу. Повинен бути у вигляді десяткового числа (наприклад, 0.05 для 5%).

        Повертає:
        None - змінює баланс обекта.
        """
        self.balance.amount = self.balance.amount + (self.balance.amount * (percent / 100))



account6 = NewBankAccount(10000, 10000, "Ivan Savcenko", "UAH", 500, 10 )
account7 = NewBankAccount(60000, 15000, 'John Doe', 'USD', 500, 10)
# print(account6)
# account6.transfer(account7, 100)
print(account6)
account6.add_percent_balance(50)
print(account6)
