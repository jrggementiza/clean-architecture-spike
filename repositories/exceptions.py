class DoesNotExist(Exception):
    def __init__(self, entity_type, entity_id, message=None):
        self.entity_type = entity_type
        self.entity_id = entity_id
        if message is None:
            message = f"{self.entity_type} {self.entity_id} does not exist"
        super().__init__(message)
