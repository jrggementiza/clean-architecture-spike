from decimal import Decimal

import pytest

from entities.transaction import Transaction
from repositories.transaction_repository import TransactionRepository
from repositories.exceptions import DoesNotExist


@pytest.fixture
def transaction_repository():
    return TransactionRepository()


def test_create_transaction(transaction_repository):
    transaction = Transaction(
        account_id=1,
        type="Deposit",
        amount=Decimal("150.00"),
        reference_code="TEST1234",
    )
    created_transaction = transaction_repository.create(transaction)
    assert created_transaction.account_id == 1
    assert created_transaction.transaction_id is not None
    assert created_transaction.transaction_id in transaction_repository.storage


def test_created_account_id_auto_increments(transaction_repository):
    transaction_1 = Transaction(account_id=1, type="Deposit", amount=Decimal("150.00"))
    created_transaction_1 = transaction_repository.create(transaction_1)

    transaction_2 = Transaction(account_id=1, type="Deposit", amount=Decimal("150.00"))
    created_transaction_2 = transaction_repository.create(transaction_2)

    assert created_transaction_1.transaction_id != created_transaction_2.transaction_id


def test_get_by_transaction_id(transaction_repository):
    transaction_repository.storage[1] = Transaction(
        transaction_id=1, account_id=1, type="Deposit", amount=Decimal("150.00")
    )

    retrieved_transaction = transaction_repository.get_by_transaction_id(1)
    assert retrieved_transaction.transaction_id == 1

    with pytest.raises(DoesNotExist):
        transaction_repository.get_by_transaction_id(99)


def test_get_by_account_id(transaction_repository):
    transaction_repository.storage[1] = Transaction(
        transaction_id=1, account_id=2, type="Deposit", amount=Decimal("150.00")
    )

    retrieved_transactions = transaction_repository.get_by_account_id(2)
    retrieved_transaction = retrieved_transactions[0]
    assert retrieved_transaction.transaction_id == 1
    assert retrieved_transaction.account_id == 2

    assert transaction_repository.get_by_account_id(99) == []
