class Customer:
    def __init__(
        self,
        name,
        email,
        phone_number,
        customer_id=None,
    ):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.customer_id = customer_id
