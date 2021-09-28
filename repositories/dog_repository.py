# repository set up for dog class
# manners of create, read, update, delete functions to be added

from db.run_sql import run_sql

from models.dog import Dog
from models.appointment import Appointment


import repositories.owner_repository as owner_repository


# SAVE dog entry
def save(dog):
    sql = "INSERT INTO dogs (name, breed, age, owner_id, comments) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [dog.name, dog.breed, dog.age, dog.owner.id, dog.comments]
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
        owner = owner_repository.select(row['owner_id'])
        dog = Dog(row['name'], row['breed'], row['age'], owner, row['comments'], row['id'])
        dogs.append(dog)
    return dogs


# SELECT dog by id
def select(id):
    dog = None
    sql = "SELECT * FROM dogs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        dog = Dog(result['name'], result['breed'], result['age'], owner, result['comments'], result['id'])
    return dog


# UPDATE dog
def update(dog):
    sql = "UPDATE dogs SET (name, breed, age, owner_id, comments) = (%s, %s, %s, %s) WHERE id = %s"
    values = [dog.name, dog.breed, dog.age, dog.owner.id, dog.comments, dog.id]
    run_sql(sql, values)


# SELECT ALL appointments by dog
def appointments(id):
    appointments = []

    sql = "SELECT * FROM appointments WHERE dog_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        appointment = Appointment(row['date'], row['time'], row['dog_id'], row['groomer_id'], row['id'])
        appointments.append(appointment)
        return appointments