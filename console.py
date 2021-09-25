# console to run functions in repositories and test

import pdb

from models.dog import Dog

import repositories.dog_repository as dog_repository

# DELETE ALL in dogs
dog_repository.delete_all()

# SAVE entries to dogs
dog1 = Dog("Biscuits", "Norfolk Terrier", 8, "Ailie", "Brown", "07930111111")
dog2 = Dog("Elvis", "Labrador", 9, "Vinnie", "Bennis", "07930222222")
dog3 = Dog("Boo", "Cocker Spaniel", 10, "Ewan", "Kelly", "07930333333")
dog_repository.save(dog1)
dog_repository.save(dog2)
dog_repository.save(dog3)

# DELETE single dog entry
dog_repository.delete(dog3.id)

# SELECT ALL in dogs
found_dogs = dog_repository.select_all()

# SELECT dog by ID
found_dog = dog_repository.select(dog1.id)

# UPDATE dog
dog1.name = "Daisy"
dog_repository.update(dog1)


pdb.set_trace()