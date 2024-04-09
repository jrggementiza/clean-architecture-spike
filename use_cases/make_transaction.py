from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"


class MakeTransactionUseCase:
    def make_transaction(self, account, transaction_type, amount):
        account_action_map = {
            TransactionType.DEPOSIT.value: "deposit",
            TransactionType.WITHDRAW.value: "withdraw",
        }

        action = account_action_map[transaction_type]
        transaction = getattr(account, action)(amount)

        # TODO: Add propagation

        return transaction