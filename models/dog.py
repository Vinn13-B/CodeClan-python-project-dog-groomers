# create Dog class with required objects

class Dog:
    
    def __init__(self, name, breed, age, owner_first_name, owner_last_name, owner_contact_number, id = None):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.owner_contact_number = owner_contact_number
        self.id = id