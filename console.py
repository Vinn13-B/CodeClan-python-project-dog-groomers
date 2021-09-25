# console to run functions in repositories and test

import pdb

from models.dog import Dog
from models.appointment import Appointment

import repositories.dog_repository as dog_repository
import repositories.appointment_repository as appointment_repository


# DELETE ALL in dogs
dog_repository.delete_all()

# DELETE ALL in appointments
appointment_repository.delete_all()

# SAVE entries to dogs
dog1 = Dog("Biscuits", "Norfolk Terrier", 8, "Ailie", "Brown", "07930111111")
dog2 = Dog("Elvis", "Labrador", 9, "Vinnie", "Bennis", "07930222222")
dog3 = Dog("Boo", "Cocker Spaniel", 10, "Ewan", "Kelly", "07930333333")
dog_repository.save(dog1)
dog_repository.save(dog2)
dog_repository.save(dog3)

# SAVE entries to appointments
appointment1 = Appointment("24/09/2021", "0800", dog1)
appointment2 = Appointment("24/09/2021", "1000", dog2)
appointment3 = Appointment("24/09/2021", "1200", dog3)
appointment_repository.save(appointment1)
appointment_repository.save(appointment2)
appointment_repository.save(appointment3)

# DELETE single dog entry
dog_repository.delete(dog3.id)

# DELETE single appointment entry
appointment_repository.delete(appointment3.id)

# SELECT ALL in dogs
found_dogs = dog_repository.select_all()

# SELECT ALL in appointments
found_appointments = appointment_repository.select_all()

# SELECT dog by id
found_dog = dog_repository.select(dog1.id)

# SELECT appointment by id
found_appointment = appointment_repository.select(appointment1.id)

# UPDATE dog
dog1.name = "Daisy"
dog_repository.update(dog1)

# UPDATE appointment
appointment1.date = "25/09/2021"
appointment_repository.update(appointment1)

# SELECT appointments by dog
dog_appointment = dog_repository.appointments(dog1)


pdb.set_trace()