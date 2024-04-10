from repositories.exceptions import DoesNotExist


class AccountRepository:
    def __init__(self):
        self.storage = {}
        self.next_id = 1  # Mocking id key increment done in db

    def create(self, account):
        account.account_id = self.next_id

        self.storage[self.next_id] = account
        self.next_id += 1
        return account

    def get_by_account_id(self, account_id):
        retrieved_account = self.storage.get(account_id, None)

        if not retrieved_account:
            raise DoesNotExist(type(self), account_id)

        return retrieved_account

    def get_by_customer_id(self, customer_id):
        # TODO: Improve customer_id traversal
        retrieved_account = [
            account
            for account in self.storage.values()
            if account.customer_id == customer_id
        ]
        if not retrieved_account:
            raise DoesNotExist(
                type(self),
                customer_id,
                f"{type(self)} with customer_id {customer_id} does not exist",
            )

        return retrieved_account[0]

    def update(self, account):
        if account.account_id not in self.storage:
            raise DoesNotExist('Account', account.account_id)

        self.storage[account.account_id] = account
Ò