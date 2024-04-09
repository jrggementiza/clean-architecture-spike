from decimal import Decimal


class Account:
    def __init__(
        self, id=None, customer_id=None, account_number=None, balance=Decimal("0.00")
    ):
        self.id = id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < Decimal("0.00"):
            raise ValueError("Negative amount not allowed")

        self.balance += amount

    def withdraw(self, amount):
        if amount < Decimal("0.00"):
            raise ValueError("Negative amount not allowed")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount