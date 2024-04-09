from entities.customer import Customer
from use_cases.create_customer import CreateCustomerUseCase


def test_create_customer():
    create_customer_use_case = CreateCustomerUseCase()
    new_customer = create_customer_use_case.create_customer("jr", "jr@yopmail.com", "+639171234567")

    assert isinstance(new_customer, Customer)
    assert new_customer.name == "jr"
    assert new_customer.email == "jr@yopmail.com"
    assert new_customer.phone_number == "+639171234567"

# TODO: Propagation
# TODO: Test auto increment of customer_id
