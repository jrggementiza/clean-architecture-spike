from entities.account import Account
from repositories.account_repository import (
    AccountRepository,
)  # TODO: plug in init by default


class CheckBalanceUseCase:
    def __init__(self, repository):
        self.account_repository = repository

    def check_balance(self, account_id):
        account = self.account_repository.get_by_account_id(account_id)

        return account.get_balance()
