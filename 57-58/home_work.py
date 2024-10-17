import unittest


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        """Инициализация банковского счета."""
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Внесение денег на счет."""
        if amount <= 0:
            return "Сумма вклада должна быть положительной."
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Снятие денег со счета."""
        if amount <= 0:
            return "Сумма снятия должна быть положительной."
        if amount > self.balance:
            return "Недостаточно средств на счете."
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Получение текущего баланса."""
        return self.balance


class TestCase(unittest.TestCase):
    def test_balance_valid(self):
        b = BankAccount('Петров', 1000)
        self.assertEqual(b.balance, 1000)

    def test_deposit_positive(self):
        b = BankAccount('Иванов', 2000)
        res = b.deposit(500)
        self.assertEqual(res, 2500)

    def test_deposit_amount_zero(self):
        b = BankAccount('Иванов', 2000)
        res = b.deposit(0)
        self.assertEqual(res, "Сумма вклада должна быть положительной.")

    def test_deposit_negative_amount(self):
        b = BankAccount('Иванов', 2000)
        res = b.deposit(-100)
        self.assertEqual(res, "Сумма вклада должна быть положительной.")

    def test_withdraw_positive(self):
        b = BankAccount('Сидоров', 5000)
        res = b.withdraw(1000)
        self.assertEqual(res, 4000)

    def test_withdraw_zero_amount(self):
        b = BankAccount('Сидоров', 5000)
        res = b.withdraw(0)
        self.assertEqual(res, "Сумма снятия должна быть положительной.")

    def test_withdraw_negative_amount(self):
        b = BankAccount('Сидоров', 5000)
        res = b.withdraw(-50)
        self.assertEqual(res, "Сумма снятия должна быть положительной.")

    def test_withdraw_not_enough_money(self):
        b = BankAccount('Сидоров', 50)
        res = b.withdraw(100)
        self.assertEqual(res, "Недостаточно средств на счете.")

    def test_get_balance(self):
        b = BankAccount('Петров', 1000)
        res = b.get_balance()
        self.assertEqual(res, 1000)
