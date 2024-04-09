from decimal import Decimal

import pytest

from entities.account import Account
from entities.transaction import Transaction
from use_cases.make_transaction import MakeTransactionUseCase


@pytest.fixture
def new_account():
    return Account(1, 1, "TEST1234")


def test_make_transaction(new_account):
    make_transaction_use_case = MakeTransactionUseCase()  # TODO: Add repository and propagation

    deposit_1 = Decimal('3.00')
    transaction = make_transaction_use_case.make_transaction(new_account, "Deposit", deposit_1)

    assert isinstance(transaction, Transaction)
    assert transaction.type == "Deposit"
    assert new_account.get_balance() == deposit_1

    withdraw_1 = Decimal('1.00')
    transaction = make_transaction_use_case.make_transaction(new_account, "Withdraw", withdraw_1)

    assert isinstance(transaction, Transaction)
    assert transaction.type == "Withdraw"
    assert new_account.get_balance() == Decimal('2.00')

    withdraw_2 = Decimal('3.00')
    with pytest.raises(ValueError):
            make_transaction_use_case.make_transaction(new_account, "Withdraw", withdraw_2)

    assert new_account.get_balance() == Decimal('2.00')
