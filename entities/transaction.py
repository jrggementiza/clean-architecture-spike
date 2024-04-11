import random


class Transaction:
    def __init__(self, account_id, type, amount, reference_code=None, transaction_id=None):
        self.account_id = account_id
        self.type = type
        self.amount = amount
        self.reference_code = reference_code or self._generate_reference_code()
        self.transaction_id = transaction_id

    def __repr__(self):
        return f"{self.type.title()} {self.amount} | Reference Code: {self.reference_code}"

    def _generate_reference_code(self):
        return "".join(random.choices("0123456789", k=6))
