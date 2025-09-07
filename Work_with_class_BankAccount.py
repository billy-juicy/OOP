class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return None

    def withdraw(self, other_amount):
        if other_amount > 0 and other_amount <= self.balance:
            self.balance -= other_amount
            return self.balance
        else:
            self.balance -= other_amount
            return self.check_balance()

    def check_balance(self):
        if self.balance < 0:
            return f'Предупреждение, у вас отрицательный баланс - {self.balance}'
        else:
            return f'Ваш баланс - {self.balance}'

account_1 = BankAccount(100)
print(account_1.deposit(100))
print(account_1.deposit(200))
print(account_1.withdraw(400))
print(account_1.withdraw(100))
print(account_1.deposit(-200))
