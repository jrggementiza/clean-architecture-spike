from decimal import Decimal

import pytest

from entities.account import Account
from entities.transaction import Transaction
from use_cases.generate_account_statements import GenerateStatementsUseCase
from repositories.transaction_repository import TransactionRepository


@pytest.fixture
def new_account():
    return Account(1, 1, "TEST1234")


@pytest.fixture
def transaction_repository():
    return TransactionRepository()


def test_generate_statement(new_account, transaction_repository):
    generate_statements_use_case = GenerateStatementsUseCase(transaction_repository)

    transaction_repository.storage = {
        1: Transaction(new_account.account_id, "Deposit", Decimal("500.00")),
        2: Transaction(new_account.account_id, "Deposit", Decimal("500.00")),
        3: Transaction(new_account.account_id, "Deposit", Decimal("500.00")),
        4: Transaction(account_id=99, type="Deposit", amount=Decimal("500.00")),
    }

    transactions = generate_statements_use_case.generate_statements(
        new_account.account_id
    )

    assert isinstance(transactions, list)
    assert len(transactions) == 3
