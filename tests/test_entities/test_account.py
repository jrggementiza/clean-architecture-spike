from decimal import Decimal

import pytest

from entities.account import Account


@pytest.fixture
def new_account():
    return Account(1, 1, "TEST1234")


def test_account_creation():
    account = Account(1, 1, "TEST1234")

    assert account.id == 1
    assert account.customer_id == 1
    assert account.account_number == "TEST1234"
    assert account.balance == Decimal("0.00")


def test_account_get_balance(new_account):
    amount = Decimal("10000.00")
    new_account.balance = amount

    assert new_account.get_balance() == amount


def test_account_deposit(new_account):
    amount = Decimal("10000.00")
    new_account.deposit(amount)

    # TODO: Add return Transaction behavior
    assert new_account.balance == amount


def test_account_not_accept_negative_deposits(new_account):
    negative_amount = Decimal("-1.00")
    with pytest.raises(ValueError):
        new_account.deposit(negative_amount)


def test_account_withdraw(new_account):
    starting_balance = Decimal("10000.00")
    withdraw_amount = Decimal("4000.00")

    new_account.balance = starting_balance
    new_account.withdraw(withdraw_amount)

    # TODO: Add return Transaction behavior
    assert new_account.balance == starting_balance - withdraw_amount


def test_account_not_accept_negative_withdraw(new_account):
    negative_amount = Decimal("-1.00")
    with pytest.raises(ValueError):
        new_account.withdraw(negative_amount)


def test_account_not_withdraw_if_no_balance(new_account):
    greater_than_balance_amount = Decimal("1.00")
    with pytest.raises(ValueError):
        new_account.withdraw(greater_than_balance_amount)
