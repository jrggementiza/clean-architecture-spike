import pytest

from entities.account import Account
from use_cases.create_account import CreateAccountUseCase
from repositories.account_repository import AccountRepository


@pytest.fixture
def account_repository():
    return AccountRepository()


def test_create_account(account_repository):
    create_account_use_case = CreateAccountUseCase(account_repository)
    new_account = create_account_use_case.create_account(1)

    assert isinstance(new_account, Account)
    assert new_account.account_id == 1
    assert new_account.customer_id == 1
    assert new_account.account_id in account_repository.storage
