from decimal import Decimal

import pytest

from bank import Bank

from entities.account import Account
from repositories.account_repository import AccountRepository
from repositories.customer_repository import CustomerRepository
from repositories.transaction_repository import TransactionRepository


@pytest.fixture
def bank_app():
    return Bank(
        AccountRepository(),
        TransactionRepository(),
        CustomerRepository(),
    )


def test_register(bank_app):
    account = bank_app.register("jr", "jr@yopmail.com", "+639112223333")

    assert isinstance(account, Account)
    assert account.account_id in bank_app.account_repository.storage
    assert account == bank_app.account_repository.storage[account.account_id]


def test_deposit(bank_app):
    account = bank_app.register("jr", "jr@yopmail.com", "+639112223333")
    txn = bank_app.deposit(account, 500)

    assert txn.amount == Decimal("500.00")
    assert txn.transaction_id in bank_app.transaction_repository.storage
    assert txn == bank_app.transaction_repository.storage[txn.transaction_id]
    assert bank_app.account_repository.storage[account.account_id].balance == Decimal(
        "500.00"
    )


def test_withdraw(bank_app):
    account = bank_app.register("jr", "jr@yopmail.com", "+639112223333")
    _ = bank_app.deposit(account, 500)
    txn = bank_app.withdraw(account, 200)

    assert txn.amount == Decimal("200.00")
    assert txn.transaction_id in bank_app.transaction_repository.storage
    assert txn == bank_app.transaction_repository.storage[txn.transaction_id]
    assert bank_app.account_repository.storage[account.account_id].balance == Decimal(
        "300.00"
    )


def test_check_balance(bank_app):
    account = bank_app.register("jr", "jr@yopmail.com", "+639112223333")
    balance = bank_app.check_balance(account)

    assert (
        balance
        == f"Account Number {account.account_number} | Balance {account.balance}"
    )


def test_generate_statements(bank_app):
    account = bank_app.register("jr", "jr@yopmail.com", "+639112223333")
    txn_1 = bank_app.deposit(account, 500)
    txn_2 = bank_app.deposit(account, 200)
    txn_3 = bank_app.withdraw(account, 100)

    assert bank_app.generate_statements(account) == "\n".join(
        [str(txn) for txn in [txn_1, txn_2, txn_3]]
    )


def test_generate_statements_no_txn(bank_app):
    account = bank_app.register("jr", "jr@yopmail.com", "+639112223333")

    assert (
        bank_app.generate_statements(account)
        == f"No Transactions for Account Number {account.account_number}"
    )
