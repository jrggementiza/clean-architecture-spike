import pytest

from entities.customer import Customer
from use_cases.create_customer import CreateCustomerUseCase
from repositories.customer_repository import CustomerRepository


@pytest.fixture
def customer_repository():
    return CustomerRepository()


def test_create_customer(customer_repository):
    create_customer_use_case = CreateCustomerUseCase(customer_repository)
    new_customer = create_customer_use_case.create_customer(
        "jr", "jr@yopmail.com", "+639171234567"
    )

    assert isinstance(new_customer, Customer)
    assert new_customer.customer_id == 1
    assert new_customer.name == "jr"
    assert new_customer.email == "jr@yopmail.com"
    assert new_customer.phone_number == "+639171234567"

    assert new_customer.customer_id in customer_repository.storage
