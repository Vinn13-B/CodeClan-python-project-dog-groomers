# console to run functions in repositories and test

import pdb

from models.dog import Dog
from models.appointment import Appointment
from models.groomer import Groomer
from models.owner import Owner


import repositories.dog_repository as dog_repository
import repositories.appointment_repository as appointment_repository
import repositories.groomer_repository as groomer_repository
import repositories.owner_repository as owner_repository


# DELETE ALL in owners
owner_repository.delete_all()

# DELETE ALL in dogs
dog_repository.delete_all()

# DELETE ALL in groomers
groomer_repository.delete_all()

# DELETE ALL in appointments
appointment_repository.delete_all()

# SAVE entries to owners
owner1 = Owner("Ailie Brown", "07933333333")
owner2 = Owner("Vinnie Bennis", "07932222222")
owner3 = Owner("Carol Ann Brown", "07934444444")
owner_repository.save(owner1)
owner_repository.save(owner2)
owner_repository.save(owner3)

# SAVE entries to dogs
dog1 = Dog("Biscuits", "Norfolk Terrier", 8, owner1)
dog2 = Dog("Elvis", "Labrador", 9, owner2)
dog3 = Dog("Boo", "Cocker Spaniel", 10, owner3)
dog_repository.save(dog1)
dog_repository.save(dog2)
dog_repository.save(dog3)

# SAVE entries to groomers
groomer1 = Groomer("Ailie", "07930444444")
groomer2 = Groomer("Victoria", "07930555555")
groomer3 = Groomer("Sarah", "07930666666")
groomer_repository.save(groomer1)
groomer_repository.save(groomer2)
groomer_repository.save(groomer3)

# SAVE entries to appointments
appointment1 = Appointment("24/09/2021", "0800", dog1, groomer1)
appointment2 = Appointment("24/09/2021", "1000", dog2, groomer1)
appointment3 = Appointment("24/09/2021", "1200", dog3, groomer2)
appointment_repository.save(appointment1)
appointment_repository.save(appointment2)
appointment_repository.save(appointment3)

# DELETE single owner entry
owner_repository.delete(owner3.id)

# DELETE single dog entry
dog_repository.delete(dog3.id)

# DELETE single appointment entry
appointment_repository.delete(appointment3.id)

# DELETE single groomer entry
groomer_repository.delete(groomer3.id)

# SELECT ALL in owners
found_owners = owner_repository.select_all()

# SELECT ALL in dogs
found_dogs = dog_repository.select_all()

# SELECT ALL in appointments
found_appointments = appointment_repository.select_all()

# SELECT ALL in groomers
found_groomers = groomer_repository.select_all()

# SELECT owner by id
found_owner = owner_repository.select(owner1.id)

# SELECT dog by id
found_dog = dog_repository.select(dog1.id)

# SELECT appointment by id
found_appointment = appointment_repository.select(appointment1.id)

# SELECT groomer by id
found_groomer = groomer_repository.select(groomer1.id)

# UPDATE owner
owner2.name = "Vincent Bennis"
owner_repository.update(owner2)

# UPDATE dog
dog1.name = "Daisy"
dog_repository.update(dog1)

# UPDATE appointment
appointment1.date = "25/09/2021"
appointment_repository.update(appointment1)

# UPDATE groomer
groomer2.name = "Jade"
groomer_repository.update(groomer2)

# SELECT dogs by owner
owner_dogs = owner_repository.dogs(owner1.id)

# SELECT appointments by dog
dog_appointments = dog_repository.appointments(dog1.id)

# SELECT appointments by groomer
groomer_appointments = groomer_repository.appointments(groomer1.id)


# deleting and repopulating db for presentation
owner_repository.delete_all()
dog_repository.delete_all()
groomer_repository.delete_all()
appointment_repository.delete_all()
owner1 = Owner("Ailie Brown", "07933333333")
owner_repository.save(owner1)
dog1 = Dog("Biscuits", "Norfolk Terrier", 8, owner1)
dog_repository.save(dog1)
groomer1 = Groomer("Ailie", "07933333333")
groomer_repository.save(groomer1)
appointment1 = Appointment("30/09/2021", "8am", dog1, groomer1)
appointment_repository.save(appointment1)

pdb.set_trace()