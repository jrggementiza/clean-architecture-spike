from decimal import Decimal

import pytest

from entities.account import Account
from repositories.account_repository import AccountRepository
from repositories.exceptions import DoesNotExist


@pytest.fixture
def account_repository():
    return AccountRepository()


def test_create_account(account_repository):
    account = Account(None, 1)
    created_account = account_repository.create(account)
    assert created_account.customer_id == 1
    assert created_account.account_id is not None
    assert created_account.account_id in account_repository.storage


def test_created_account_id_auto_increments(account_repository):
    account_1 = Account(customer_id=1)
    created_account_1 = account_repository.create(account_1)

    account_2 = Account(customer_id=2)
    created_account_2 = account_repository.create(account_2)

    assert created_account_1.account_id != created_account_2.account_id


def test_get_by_account_id(account_repository):
    account_repository.storage[1] = Account(account_id=1, customer_id=1)

    retrieved_account = account_repository.get_by_account_id(1)
    assert retrieved_account.account_id == 1

    with pytest.raises(DoesNotExist):
        retrieved_account = account_repository.get_by_account_id(99)


def test_get_by_customer_id(account_repository):
    account_repository.storage[1] = Account(account_id=1, customer_id=2)

    retrieved_account = account_repository.get_by_customer_id(2)
    assert retrieved_account.account_id == 1
    assert retrieved_account.customer_id == 2

    with pytest.raises(DoesNotExist):
        retrieved_account = account_repository.get_by_customer_id(99)


def test_update_existing_account(account_repository):
    account = Account(account_id=1, customer_id=1)
    account_repository.storage[account.account_id] = account

    account.balance = Decimal("150.00")
    account_repository.update(account)
    updated_account = account_repository.get_by_account_id(account.account_id)

    assert updated_account.balance == Decimal("150.00")
    assert account_repository.storage[account.account_id].balance == Decimal("150.00")

    # Not persisted account should not update
    not_persisted_account = Account(account_id=2, customer_id=2)
    with pytest.raises(DoesNotExist):
        account_repository.update(not_persisted_account)
