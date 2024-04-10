from repositories.transaction_repository import TransactionRepository


class GenerateStatementsUseCase:
    def __init__(self, repository):
        self.transaction_repository = repository

    def generate_statements(self, account_id):
        transactions = self.transaction_repository.get_by_account_id(account_id)
        return transactions
