from decimal import Decimal
from unittest.mock import patch

from entities.transaction import Transaction


def test_create_transaction():
    transaction = Transaction(1, "Deposit", Decimal("1.00"), "TEST1234", transaction_id=1)

    assert transaction.account_id == 1
    assert transaction.transaction_id == 1
    assert transaction.type == "Deposit"
    assert transaction.amount == Decimal("1.00")
    assert transaction.reference_code == "TEST1234"


def test_transaction_reference_code_geenerates_if_none():
    with patch.object(Transaction, '_generate_reference_code', return_value='123456'):
        transaction = Transaction(1, "Deposit", Decimal("1.00"))

        assert transaction.reference_code == "123456"
