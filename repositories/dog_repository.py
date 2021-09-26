# repository set up for dog class
# manners of create, read, update, delete functions to be added

from db.run_sql import run_sql

from models.dog import Dog
from models.appointment import Appointment


# SAVE dog entry
def save(dog):
    sql = "INSERT INTO dogs (name, breed, age, owner_first_name, owner_last_name, owner_contact_number) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [dog.name, dog.breed, dog.age, dog.owner_first_name, dog.owner_last_name, dog.owner_contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    dog.id = id
    return dog


# DELETE ALL dog entries
def delete_all():
    sql = "DELETE  FROM dogs"
    run_sql(sql)


# DELETE single dog entry
def delete(id):
    sql = "DELETE  FROM dogs WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# SELECT ALL entries in dogs
def select_all():
    dogs = []

    sql = "SELECT * FROM dogs"
    results = run_sql(sql)

    for row in results:
        dog = Dog(row['name'], row['breed'], row['age'], row['owner_first_name'], row['owner_last_name'], row['owner_contact_number'], row['id'])
        dogs.append(dog)
    return dogs


# SELECT dog by id
def select(id):
    dog = None
    sql = "SELECT * FROM dogs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        dog = Dog(result['name'], result['breed'], result['age'], result['owner_first_name'], result['owner_last_name'], result['owner_contact_number'], result['id'])
    return dog


# UPDATE dog
def update(dog):
    sql = "UPDATE dogs SET (name, breed, age, owner_first_name, owner_last_name, owner_contact_number) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [dog.name, dog.breed, dog.age, dog.owner_first_name, dog.owner_last_name, dog.owner_contact_number, dog.id]
    run_sql(sql, values)


# SELECT ALL appointments by dog
def appointments(id):
    appointments = []

    sql = "SELECT * FROM appointments WHERE dog_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        appointment = Appointment(row['date'], row['time'], row['dog_id'], row['id'])
        appointments.append(appointment)
        return appointments