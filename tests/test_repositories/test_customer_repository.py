import pytest

from entities.customer import Customer
from repositories.customer_repository import CustomerRepository
from repositories.exceptions import DoesNotExist


@pytest.fixture
def customer_repository():
    return CustomerRepository()


def test_create_customer(customer_repository):
    customer = Customer(name="jr", email="jr@yopmail.com", phone_number="+639171234567")
    created_customer = customer_repository.create(customer)

    assert created_customer.customer_id == 1
    assert created_customer.name == "jr"
    assert created_customer.email == "jr@yopmail.com"
    assert created_customer.phone_number == "+639171234567"
    assert created_customer.customer_id in customer_repository.storage


def test_created_customer_id_auto_increments(customer_repository):
    customer_1 = Customer(
        name="jr", email="jr@yopmail.com", phone_number="+639171234567"
    )
    created_customer_1 = customer_repository.create(customer_1)

    customer_2 = Customer(
        name="not jr", email="not_jr@yopmail.com", phone_number="+639171236969"
    )
    created_customer_2 = customer_repository.create(customer_2)

    assert created_customer_1.customer_id != created_customer_2.customer_id


def test_get_by_customer_id(customer_repository):
    customer_repository.storage[1] = Customer(
        name="jr", email="jr@yopmail.com", phone_number="+639171234567", customer_id=1
    )

    retrieved_customer = customer_repository.get_customer_by_id(1)
    assert retrieved_customer.customer_id == 1

    with pytest.raises(DoesNotExist):
        customer_repository.get_customer_by_id(99)


def test_update_existing_customert(customer_repository):
    customer = Customer(
        name="jr", email="jr@yopmail.com", phone_number="+639171234567", customer_id=1
    )
    customer_repository.storage[customer.customer_id] = customer

    customer.name = "not jr"
    customer_repository.update(customer)
    updated_customer = customer_repository.get_customer_by_id(customer.customer_id)

    assert updated_customer.name == "not jr"
    assert customer_repository.storage[customer.customer_id].name == "not jr"

    # Not persisted customer should not update
    not_persisted_customer = Customer(
        name="really not",
        email="really_not_jr@yopmail.com",
        phone_number="+639171239999",
        customer_id=99,
    )
    with pytest.raises(DoesNotExist):
        customer_repository.update(not_persisted_customer)
