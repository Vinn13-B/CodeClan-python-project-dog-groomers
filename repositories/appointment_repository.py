# repository set up for appointment class
# manners of create, read, update, delete functions to be added

from db.run_sql import run_sql

from models.dog import Dog
from models.appointment import Appointment
import repositories.dog_repository as dog_repository


# SAVE appointment entry
def save(appointment):
    sql = "INSERT INTO appointments (date, time, dog_id) VALUES (%s, %s, %s) RETURNING *"
    values = [appointment.date, appointment.time, appointment.dog.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    appointment.id = id
    return appointment


# DELETE ALL appointments entries
def delete_all():
    sql = "DELETE  FROM appointments"
    run_sql(sql)


# DELETE single appointment entry
def delete(id):
    sql = "DELETE  FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# SELECT ALL entries in appointments
def select_all():
    appointments = []

    sql = "SELECT * FROM appointments"
    results = run_sql(sql)

    for row in results:
        dog = dog_repository.select(row['dog_id'])
        appointment = Appointment(row['date'], row['time'], dog, row['id'])
        appointments.append(appointment)
    return appointments


# SELECT appointment by id
def select(id):
    appointment = None
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        dog = dog_repository.select(result['dog_id'])
        appointment = Appointment(result['date'], result['time'], dog, result['id'])
    return appointment


# UPDATE appointment
def update(appointment):
    sql = "UPDATE appointments SET (date, time, dog_id) = (%s, %s, %s) WHERE id = %s"
    values = [appointment.date, appointment.time, appointment.dog.id, appointment.id]
    run_sql(sql, values)
