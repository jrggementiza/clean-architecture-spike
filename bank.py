from decimal import Decimal

from entities.account import Account
from entities.transaction import Transaction
from use_cases.create_account import CreateAccountUseCase
from use_cases.create_customer import CreateCustomerUseCase
from use_cases.make_transaction import MakeTransactionUseCase
from use_cases.generate_account_statements import GenerateStatementsUseCase
from use_cases.check_balance import CheckBalanceUseCase
from repositories.account_repository import AccountRepository
from repositories.customer_repository import CustomerRepository
from repositories.transaction_repository import TransactionRepository


class Bank:
    def __init__(
        self,
        account_repository=None,
        transaction_repository=None,
        customer_repository=None,
    ):
        self.account_repository = account_repository or AccountRepository()
        self.transaction_repository = transaction_repository or TransactionRepository()
        self.customer_repository = customer_repository or CustomerRepository()

        self.create_customer_use_case = CreateCustomerUseCase(self.customer_repository)
        self.make_transaction_use_case = MakeTransactionUseCase(
            self.transaction_repository
        )
        self.generate_statements_use_case = GenerateStatementsUseCase(
            self.transaction_repository
        )
        self.create_account_use_case = CreateAccountUseCase(self.account_repository)
        self.check_balance_use_case = CheckBalanceUseCase(self.account_repository)

    def register(self, name, email, phone_number) -> Account:
        created_customer = self.create_customer_use_case.create_customer(
            name, email, phone_number
        )
        return self.create_account_use_case.create_account(created_customer.customer_id)

    def deposit(self, account: Account, amount: Decimal) -> Transaction:
        amount = Decimal(amount)
        return self.make_transaction_use_case.make_transaction(
            account, "Deposit", amount
        )

    def withdraw(self, account: Account, amount: Decimal) -> Transaction:
        amount = Decimal(amount)
        return self.make_transaction_use_case.make_transaction(
            account, "Withdraw", amount
        )

    def check_balance(self, account) -> str:
        balance = self.check_balance_use_case.check_balance(account.account_id)
        return f"Account Number {account.account_number} | Balance {balance}"

    def generate_statements(self, account) -> str:
        transactions = self.generate_statements_use_case.generate_statements(
            account.account_id
        )

        if not transactions:
            return f"No Transactions for Account Number {account.account_number}"

        formatted_txns = "\n".join([str(txn) for txn in transactions])
        return formatted_txns
