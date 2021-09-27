# create Dog class with required objects

class Dog:
    
    def __init__(self, name, breed, age, owner, comments, id = None):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner
        self.comments = comments
        self.id = id