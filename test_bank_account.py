import unittest
from Work_with_class_BankAccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = BankAccount(100)  # Создаем счет с балансом 100
        self.assertEqual(account.balance, 100)  # Проверяем равенство

    def test_deposit(self):
        account = BankAccount(200)  # Создаем счет с балансом 200
        result = account.deposit(200)  # Вносим на баланс 200
        self.assertEqual(result, 400)  # Проверяем равенство

    def test_withdraw(self):
        account = BankAccount(400)  # Создаем счет с балансом 400
        result = account.withdraw(500)  # Пытаемся снять 500 (больше чем есть)
        self.assertEqual(result, 'Предупреждение, у вас отрицательный баланс - -100')


if __name__ == '__main__':
    unittest.main()
