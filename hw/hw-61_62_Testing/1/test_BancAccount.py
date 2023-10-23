import unittest
from BankAccount import BankAccount, Money

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Підготовка до тестів, створення тестових об'єктів
        self.account1 = BankAccount(10000, 100, 'Ivan Sacvhenko1', 'USD')
        self.account2 = BankAccount(20000, 100, 'Madaminova Ludmila', 'EUR')

    def test_transfer(self):
        # Перевірка правильності переказу коштів
        self.assertTrue(self.account1.transfer(self.account2, Money(10, 'USD')))
        self.assertEqual(self.account1.balance.amount, 90)
        self.assertEqual(self.account2.balance.amount, 110)

    def test_transfer_funds(self):
        # Перевірка правильності переказу коштів з урахуванням курсу валют
        self.assertTrue(self.account1.transfer_funds(self.account2, 10))
        self.assertAlmostEqual(self.account1.balance.amount, 90)
        self.assertAlmostEqual(self.account2.balance.amount, 110)

    def test_delete_account(self):
        # Перевірка видалення рахунку
        self.assertTrue(BankAccount.delete_account(self.account1.account_number))
        self.assertIsNone(BankAccount.load_from_file(self.account1.account_number))

    def tearDown(self):
        # Завершення тестів, видалення тестових об'єктів
        BankAccount.delete_account(self.account1.account_number)
        BankAccount.delete_account(self.account2.account_number)

if __name__ == '__main__':
    unittest.main()