from entities.customer import Customer
from repositories.customer_repository import CustomerRepository


class CreateCustomerUseCase:
    def __init__(self, repository):
        self.customer_repository = repository

    def create_customer(self, name, email, phone_number):
        customer = Customer(name, email, phone_number)
        saved_customer = self.customer_repository.create(customer)
        return saved_customer
