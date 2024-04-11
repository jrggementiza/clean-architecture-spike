from decimal import Decimal

import pytest

from entities.account import Account
from use_cases.check_balance import CheckBalanceUseCase
from repositories.account_repository import AccountRepository


@pytest.fixture
def account_repository():
    return AccountRepository()


@pytest.fixture
def new_account():
    return Account(1, 1, "TEST1234")


def test_check_balance(new_account, account_repository):
    check_balance_use_case = CheckBalanceUseCase(account_repository)
    account_repository.storage[new_account.account_id] = new_account

    assert check_balance_use_case.check_balance(new_account.account_id) == Decimal(
        "0.00"
    )
