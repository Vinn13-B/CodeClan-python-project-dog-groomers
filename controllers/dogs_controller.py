# controller and routes for dogs

from flask import Blueprint, Flask, redirect, render_template, request

from models.dog import Dog
from models.appointment import Appointment
import repositories.dog_repository as dog_repository
import repositories.appointment_repository as appointment_repository
import repositories.owner_repository as owner_repository
import repositories.groomer_repository as groomer_repository

dogs_blueprint = Blueprint("dogs", __name__)


# SELECT ALL dogs
# index
@dogs_blueprint.route("/dogs")
def dogs():
    dogs = dog_repository.select_all()
    owners = owner_repository.select_all()
    return render_template("dogs/index.html", dogs=dogs, owners=owners)


# SELECT dog by id
# show
@dogs_blueprint.route("/dogs/<id>")
def show_dog(id):
    dog = dog_repository.select(id)
    appointments = dog_repository.appointments(id)
    dogs = dog_repository.select_all()
    groomers = groomer_repository.select_all()
    return render_template("dogs/show.html", dog=dog, appointments=appointments, dogs=dogs, groomers=groomers)


# EDIT dog
# edit
@dogs_blueprint.route("/dogs/<id>/edit", methods=["POST"])
def edit_dog(id):
    dog = dog_repository.select(id)
    owners = owner_repository.select_all()
    return render_template("dogs/edit.html", dog=dog, owners=owners)


# UPDATE dog
@dogs_blueprint.route("/dogs/<id>", methods=["POST"])
def update_dog(id):
    name = request.form["name"]
    breed = request.form["breed"]
    age = request.form["age"]
    owner_id = request.form["owner_id"]
    owner = owner_repository.select(owner_id)
    dog = Dog(name, breed, age, owner, id)
    dog_repository.update(dog)
    return render_template("/dogs/show.html", dog=dog)


# DELETE dog
@dogs_blueprint.route("/dogs/<id>/delete", methods=["POST"])
def delete_dog(id):
    dog_repository.delete(id)
    return redirect("/dogs")


# SAVE new dog
@dogs_blueprint.route("/dogs", methods=["POST"])
def create_dog():
    name = request.form["name"]
    breed = request.form["breed"]
    age = request.form["age"]
    owner_id = request.form["owner_id"]
    owner = owner_repository.select(owner_id)
    new_dog = Dog(name, breed, age, owner, id)
    dog_repository.save(new_dog)
    return redirect("/dogs")


# SAVE new appointment from dog show
@dogs_blueprint.route("/dogs/appointment", methods=["POST"])
def create_appointment():
    date = request.form["date"]
    time = request.form["time"]
    dog_id = request.form["dog_id"]
    dog = dog_repository.select(dog_id)
    groomer_id = request.form["groomer_id"]
    groomer = groomer_repository.select(groomer_id)
    new_appointment = Appointment(date, time, dog, groomer)
    appointment_repository.save(new_appointment)
    appointments = dog_repository.appointments(dog_id)
    dogs = dog_repository.select_all()
    groomers = groomer_repository.select_all()
    return render_template("/dogs/show.html", dog=dog, appointments=appointments, groomers=groomers, dogs=dogs,)
