# create Owner class with required objects

class Owner:

    def __init__(self, name, contact_number, id = None):
        self.name = name
        self.contact_number = contact_number
        self.id = id