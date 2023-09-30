class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"


class BankAccount:
    accounts = []

    def __init__(self, account_number, balance, owner_name, currency):
        self.account_number = account_number
        self.balance = Money(balance, currency)
        self.owner_name = owner_name
        BankAccount.accounts.append(self)

    def transfer(self, recipient_account, money):
        """
        Переказує гроші з поточного рахунку на рахунок отримувача.

        Параметри:
        recipient_account (BankAccount): Рахунок отримувача.
        money (Money): Сума грошей та валюта для переказу.

        Повертає:
        None
        """
        if self.balance.currency != recipient_account.balance.currency:
            print("Неможливо здійснити переказ між рахунками з різними валютами.")
            return

        if money.amount < 0:
            print("Сума переказу не може бути від'ємною!")

        if money.amount <= self.balance.amount:
            self.balance.amount -= money.amount
            recipient_account.balance.amount += money.amount
            print("Переказ здійснено успішно")
        else:
            print(f"На рахунку {self.owner_name} недостатньо коштів, поточний баланс = {self.balance.amount}")


# Приклад використання
account1 = BankAccount(10000, 100, 'Ivan Sacvhenko', 'USD')
account2 = BankAccount(20000, 100, 'Madaminova Ludmila', 'EUR')

# Спроба переказу між рахунками з різними валютами
account1.transfer(account2, Money(50, 'USD'))

# Спроба переказу зі спільною валютою
account1.transfer(account2, Money(30, 'USD'))

# Виведення балансів
print("Баланс рахунку 1:", account1.balance)
print("Баланс рахунку 2:", account2.balance)
