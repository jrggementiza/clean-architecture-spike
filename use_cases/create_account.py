from entities.account import Account


class CreateAccountUseCase:
    def create_account(self, customer_id):
        # TODO: Add propagation
        # TODO: Add auto increment of account_id
        return Account(None, customer_id)
