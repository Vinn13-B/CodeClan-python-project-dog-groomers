# repository set up for appointment class
# manners of create, read, update, delete functions to be added

from db.run_sql import run_sql
import datetime

from models.appointment import Appointment

import repositories.dog_repository as dog_repository
import repositories.groomer_repository as groomer_repository


# SAVE appointment entry
def save(appointment):
    sql = "INSERT INTO appointments (date, time, dog_id, groomer_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [appointment.date, appointment.time, appointment.dog.id, appointment.groomer.id]
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
        groomer = groomer_repository.select(row['groomer_id'])
        appointment = Appointment(row['date'], row['time'], dog, groomer, row['id'])
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
        groomer = groomer_repository.select(result['groomer_id'])
        appointment = Appointment(result['date'], result['time'], dog, groomer, result['id'])
    return appointment


# UPDATE appointment
def update(appointment):
    sql = "UPDATE appointments SET (date, time, dog_id, groomer_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [appointment.date, appointment.time, appointment.dog.id, appointment.groomer.id, appointment.id]
    run_sql(sql, values)


# SELECT appointments today
def today():
    appointments = []
    today = datetime.datetime.now()
    now = today.strftime("%Y-%m-%d")

    sql = "SELECT * FROM appointments WHERE date = %s"
    values = [now]
    results = run_sql(sql, values)

    for row in results:
        appointment = Appointment(row['date'], row['time'], row['dog_id'], row['groomer_id'], row['id'])
        appointments.append(appointment)
    return appointments


# SELECT appointments for date range
def date_range(date_from, date_to):
    appointments = []
    sql = "SELECT * FROM appointments WHERE date >= %s and date <= %s"
    values = [date_from, date_to]
    results = run_sql(sql, values)

    for row in results:
        dog = dog_repository.select(row['dog_id'])
        groomer = groomer_repository.select(row['groomer_id'])
        appointment = Appointment(row['date'], row['time'], dog, groomer, row['id'])
        appointments.append(appointment)
    return appointments
