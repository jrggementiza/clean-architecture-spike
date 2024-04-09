from entities.account import Account
from use_cases.create_account import CreateAccountUseCase


def test_create_account():
    create_account_use_case = CreateAccountUseCase()
    new_account = create_account_use_case.create_account(1)

    assert isinstance(new_account, Account)
    assert new_account.customer_id == 1

# TODO: Propagation
# TODO: Test auto increment of account_id
