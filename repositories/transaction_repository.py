from repositories.exceptions import DoesNotExist


class TransactionRepository:
    def __init__(self):
        self.storage = {}
        self.next_id = 1  # Mocking id key increment done in db

    def create(self, transaction):
        transaction.transaction_id = self.next_id

        self.storage[self.next_id] = transaction
        self.next_id += 1
        return transaction

    def get_by_transaction_id(self, transaction_id):
        retrieved_transaction = self.storage.get(transaction_id, None)

        if not retrieved_transaction:
            raise DoesNotExist(type(self), transaction_id)

        return retrieved_transaction

    def get_by_account_id(self, account_id):
        # TODO: Improve account_id traversal
        retrieved_transactions = [
            txn for txn in self.storage.values() if txn.account_id == account_id
        ]

        return retrieved_transactions or []
