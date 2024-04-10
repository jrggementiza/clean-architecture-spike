from decimal import Decimal

import pytest

from entities.account import Account
from entities.transaction import Transaction
from use_cases.make_transaction import MakeTransactionUseCase
from repositories.transaction_repository import TransactionRepository


@pytest.fixture
def transaction_repository():
    return TransactionRepository()


@pytest.fixture
def new_account():
    return Account(1, 1, "TEST1234")


def test_make_transaction(new_account, transaction_repository):
    make_transaction_use_case = MakeTransactionUseCase(transaction_repository)

    deposit_1 = Decimal("3.00")
    transaction_1 = make_transaction_use_case.make_transaction(
        new_account, "Deposit", deposit_1
    )

    assert isinstance(transaction_1, Transaction)
    assert transaction_1.transaction_id == 1
    assert transaction_1.type == "Deposit"
    assert new_account.get_balance() == deposit_1

    withdraw_1 = Decimal("1.00")
    transaction_2 = make_transaction_use_case.make_transaction(
        new_account, "Withdraw", withdraw_1
    )

    assert isinstance(transaction_2, Transaction)
    assert transaction_2.transaction_id == 2
    assert transaction_2.type == "Withdraw"
    assert new_account.get_balance() == Decimal("2.00")

    withdraw_2 = Decimal("3.00")
    with pytest.raises(ValueError):
        make_transaction_use_case.make_transaction(new_account, "Withdraw", withdraw_2)

    assert new_account.get_balance() == Decimal("2.00")

    assert transaction_1.transaction_id in transaction_repository.storage
    assert transaction_2.transaction_id in transaction_repository.storage
