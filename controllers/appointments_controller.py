# controller and routes for appointments

from flask import Blueprint, Flask, redirect, render_template, request

from models.appointment import Appointment
from models.dog import Dog
from models.groomer import Groomer

import repositories.appointment_repository as appointment_repository
import repositories.dog_repository as dog_repository
import repositories.groomer_repositories as groomer_repository

appointments_blueprint = Blueprint("appointments", __name__)


# SELECT ALL appointments
# index
@appointments_blueprint.route("/appointments")
def apointments():
    appointments = appointment_repository.select_all()
    return render_template("appointments/index.html", appointments=appointments)


# SELECT appointment by id
# show
@appointments_blueprint.route("/appointments/<id>")
def show_appointment(id):
    appointment = appointment_repository.select(id)
    return render_template("appointments/show.html", appointment=appointment)


# EDIT appointment
# edit
@appointments_blueprint.route("/appointments/<id>/edit", methods=["POST"])
def edit_appointment(id):
    appointment = appointment_repository.select(id)
    dogs = dog_repository.select_all()
    groomers = groomer_repository.select_all()
    return render_template("appointments/edit.html", appointment=appointment, dogs=dogs, groomers=groomers)


# UPDATE appointment
@appointments_blueprint.route("/appointments/<id>", methods=["POST"])
def update_appointment(id):
    date = request.form["date"]
    time = request.form["time"]
    dog_id = request.form["dog_id"]
    dog = dog_repository.select(dog_id)
    groomer_id = request.form["groomer_id"]
    groomer = groomer_repository.select(groomer_id)
    appointment = Appointment(date, time, dog, groomer, id)
    appointment_repository.update(appointment)
    return redirect("/appointments")


# DELETE appointment
@appointments_blueprint.route("/appointments/<id>/delete", methods=["POST"])
def delete_appointment(id):
    appointment_repository.delete(id)
    return redirect("/appointments")


# create new appointment
# new
@appointments_blueprint.route("/appointments/new")
def new_appointment():
    dogs = dog_repository.select_all()
    groomers = groomer_repository.select_all()
    return render_template("/appointments/new.html", dogs=dogs, groomers=groomers)


# SAVE new appointment
@appointments_blueprint.route("/appointments", methods=["POST"])
def create_appointment():
    date = request.form["date"]
    time = request.form["time"]
    dog_id = request.form["dog_id"]
    dog = dog_repository.select(dog_id)
    groomer_id = request.form["groomer_id"]
    groomer = groomer_repository.select(groomer_id)
    new_appointment = Appointment(date, time, dog, groomer)
    appointment_repository.save(new_appointment)
    return redirect("/appointments")