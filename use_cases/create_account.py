from entities.account import Account
from repositories.account_repository import (
    AccountRepository,
)  # TODO: plug in init by default


class CreateAccountUseCase:
    def __init__(self, repository):
        self.account_repository = repository

    def create_account(self, customer_id):
        account = Account(None, customer_id)
        saved_account = self.account_repository.create(account)

        return saved_account
