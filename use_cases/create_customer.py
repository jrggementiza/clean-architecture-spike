from entities.customer import Customer


class CreateCustomerUseCase:
    def create_customer(self, name, email, phone_number):
        # TODO: Add propagation
        # TODO: Add auto increment of customer_id
        return Customer(name, email, phone_number)
