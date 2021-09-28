# controller and routes for groomers

from flask import Blueprint, Flask, redirect, render_template, request

from models.dog import Dog
from models.appointment import Appointment
from models.groomer import Groomer

import repositories.dog_repository as dog_repository
import repositories.appointment_repository as appointment_repository
import repositories.groomer_repository as groomer_repository

groomers_blueprint = Blueprint("groomers", __name__)


# SELECT ALL groomers
# index
@groomers_blueprint.route("/groomers")
def groomers():
    groomers = groomer_repository.select_all()
    return render_template("groomers/index.html", groomers=groomers)


# SELECT groomer by id
# show
@groomers_blueprint.route("/groomers/<id>")
def show_groomer(id):
    groomer = groomer_repository.select(id)
    appointments = groomer_repository.appointments(id)
    dogs = dog_repository.select_all()
    return render_template("groomers/show.html", groomer=groomer, appointments=appointments, dogs=dogs)


# EDIT groomer
# edit
@groomers_blueprint.route("/groomers/<id>/edit", methods=["POST"])
def edit_groomer(id):
    groomer = groomer_repository.select(id)
    return render_template("groomers/edit.html", groomer=groomer)


# UPDATE groomer
@groomers_blueprint.route("/groomers/<id>", methods=["POST"])
def update_groomer(id):
    name = request.form["name"]
    contact_number = request.form["contact_number"]
    groomer = Groomer(name, contact_number, id)
    groomer_repository.update(groomer)
    appointments = groomer_repository.appointments(id)
    dogs = dog_repository.select_all()
    return render_template("/groomers/show.html", groomer=groomer, appointments=appointments, dogs=dogs)


# DELETE groomer
@groomers_blueprint.route("/groomers/<id>/delete", methods=["POST"])
def delete_groomer(id):
    groomer_repository.delete(id)
    return redirect("/groomers")

# SAVE new groomer
@groomers_blueprint.route("/groomers", methods=["POST"])
def create_groomer():
    name = request.form["name"]
    contact_number = request.form["contact_number"]
    new_groomer = Groomer(name, contact_number)
    groomer_repository.save(new_groomer)
    return redirect("/groomers")