from repositories.exceptions import DoesNotExist


class CustomerRepository:
    def __init__(self):
        self.storage = {}
        self.next_id = 1  # Mocking id key increment done in db

    def create(self, customer):
        customer.customer_id = self.next_id

        self.storage[self.next_id] = customer
        self.next_id += 1
        return customer

    def get_customer_by_id(self, customer_id):
        retrieved_customer = self.storage.get(customer_id, None)

        if not retrieved_customer:
            raise DoesNotExist(type(self), customer_id)

        return retrieved_customer

    def update(self, customer):
        if customer.customer_id not in self.storage:
            raise DoesNotExist("Customer", customer.customer_id)

        self.storage[customer.customer_id] = customer
