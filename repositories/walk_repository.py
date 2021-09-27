# repository set up for walk class
# manners of create, read, update, delete functions to be added

from db.run_sql import run_sql

from models.dog import Dog
from models.owner import Owner
from models.walk import Walk

import repositories.owner_repository as owner_repository
import repositories.dog_repository as dog_repository


# SAVE walk entry
def save(walk):
    sql = "INSERT INTO walks (date, time, capacity, dog_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [walk.date, walk.time, walk.capacity, walk.dog.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    walk.id = id
    return walk


# DELETE ALL walk entries
def delete_all():
    sql = "DELETE  FROM walks"
    run_sql(sql)


# DELETE single walk entry
def delete(id):
    sql = "DELETE  FROM walks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# SELECT ALL entries in walks
def select_all():
    walks = []

    sql = "SELECT * FROM walks"
    results = run_sql(sql)

    for row in results:
        dog = dog_repository.select(row['dog_id'])
        walk = Walk(row['date'], row['time'], row['capacity'], dog, row['id'])
        walks.append(walk)
    return walks


# SELECT walk by id
def select(id):
    walk = None
    sql = "SELECT * FROM walks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        dog = dog_repository.select(result['dog_id'])
        walk = Walk(result['date'], result['time'], result['capacity'], dog)
    return walk


# UPDATE walk
def update(walk):
    sql = "UPDATE walks SET (date, time, capacity, dog_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [walk.date, walk.time, walk.capacity, walk.dog.id, walk.id]
    run_sql(sql, values)


# SELECT ALL dogs by walk
def dogs(id):
    dogs = []

    sql = "SELECT * FROM dogs WHERE walk_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        dog = Dog(row['name'], row['breed'], row['age'], row['owner_id'], row['comments'], row['id'])
        dogs.append(dog)
        return dogs