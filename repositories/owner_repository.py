# repository set up for Owner class
# manners of create, read, update, delete functions to be added

from db.run_sql import run_sql

from models.dog import Dog
from models.appointment import Appointment
from models.groomer import Groomer
from models.owner import Owner

# SAVE owner entry
def save(owner):
    sql = "INSERT INTO owners (name, contact_number) VALUES (%s, %s) RETURNING *"
    values = [owner.name, owner.contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner


# DELETE ALL owner entries
def delete_all():
    sql = "DELETE  FROM owners"
    run_sql(sql)


# DELETE single owner entry
def delete(id):
    sql = "DELETE  FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# SELECT ALL entries in owners
def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['name'], row['contact_number'], row['id'])
        owners.append(owner)
    return owners


# SELECT owner by id
def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['name'], result['contact_number'], result['id'])
    return owner


# UPDATE owner
def update(owner):
    sql = "UPDATE owners SET (name, contact_number) = (%s, %s) WHERE id = %s"
    values = [owner.name, owner.contact_number, owner.id]
    run_sql(sql, values)


# SELECT ALL dogs by owner
def dogs(id):
    dogs = []

    sql = "SELECT * FROM dogs WHERE owner_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        dog = Dog(row['name'], row['breed'], row['age'], row['owner_id'], row['comments'], row['id'])
        dogs.append(dog)
    return dogs