import random
from decimal import Decimal


from .transaction import Transaction


class Account:
    def __init__(
        self,
        account_id=None,
        customer_id=None,
        account_number=None,
        balance=Decimal("0.00"),
    ):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number or self._generate_account_number()
        self.balance = balance

    def _generate_account_number(self):
        return "".join(random.choices("0123456789", k=12))

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < Decimal("0.00"):
            raise ValueError("Negative amount not allowed")

        self.balance += amount

        return Transaction(self.account_id, "Deposit", amount)

    def withdraw(self, amount):
        if amount < Decimal("0.00"):
            raise ValueError("Negative amount not allowed")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount

        return Transaction(self.account_id, "Withdraw", amount)
