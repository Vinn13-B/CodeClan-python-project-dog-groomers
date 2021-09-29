# create Dog class with required objects

class Dog:
    
    def __init__(self, name, breed, age, owner, id = None):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner
        self.id = id