# repository set up for groomer class
# manners of create, read, update, delete functions to be added

from db.run_sql import run_sql

from models.appointment import Appointment
from models.groomer import Groomer


# SAVE groomer entry
def save(groomer):
    sql = "INSERT INTO groomers (name, contact_number) VALUES (%s, %s) RETURNING *"
    values = [groomer.name, groomer.contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    groomer.id = id
    return groomer


# DELETE ALL groomer entries
def delete_all():
    sql = "DELETE  FROM groomers"
    run_sql(sql)


# DELETE single groomer entry
def delete(id):
    sql = "DELETE  FROM groomers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# SELECT ALL entries in groomers
def select_all():
    groomers = []

    sql = "SELECT * FROM groomers"
    results = run_sql(sql)

    for row in results:
        groomer = Groomer(row['name'], row['contact_number'], row['id'])
        groomers.append(groomer)
    return groomers


# SELECT groomer by id
def select(id):
    groomer = None
    sql = "SELECT * FROM groomers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        groomer = Groomer(result['name'], result['contact_number'], result['id'])
    return groomer


# UPDATE groomer
def update(groomer):
    sql = "UPDATE groomers SET (name, contact_number) = (%s, %s) WHERE id = %s"
    values = [groomer.name, groomer.contact_number, groomer.id]
    run_sql(sql, values)


# SELECT ALL appointments by groomer
def appointments(id):
    appointments = []

    sql = "SELECT * FROM appointments WHERE groomer_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        appointment = Appointment(row['date'], row['time'], row['dog_id'], row['groomer_id'], row['id'])
        appointments.append(appointment)
    return appointments