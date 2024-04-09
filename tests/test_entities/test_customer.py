from entities.customer import Customer


def test_create_customer():
    customer = Customer("jr", "jr@yopmail.com", "+639171234567", 1)

    assert customer.name == "jr"
    assert customer.email == "jr@yopmail.com"
    assert customer.phone_number == "+639171234567"
    assert customer.customer_id == 1
