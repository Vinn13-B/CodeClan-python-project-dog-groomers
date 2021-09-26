# controller and routes for dogs

from flask import Blueprint, Flask, redirect, render_template, request

from models.dog import Dog
from models.appointment import Appointment
import repositories.dog_repository as dog_repository
import repositories.appointment_repository as appointment_repository

dogs_blueprint = Blueprint("dogs", __name__)

# SELECT ALL dogs
# index
@dogs_blueprint.route("/dogs")
def dogs():
    dogs = dog_repository.select_all()
    return render_template("dogs/index.html", dogs=dogs)


# SELECT dog by id
# show
@dogs_blueprint.route("/dogs/<id>")
def show_dog(id):
    dog = dog_repository.select(id)
    appointments = dog_repository.appointments(id)
    return render_template("dogs/show.html", dog=dog, appointments=appointments)


# EDIT dog
# edit
@dogs_blueprint.route("/dogs/<id>/edit", methods=["POST"])
def edit_dog(id):
    dog = dog_repository.select(id)
    return render_template("dogs/edit.html", dog=dog)


# UPDATE dog
@dogs_blueprint.route("/dogs/<id>", methods=["POST"])
def update_dog(id):
    name = request.form["name"]
    breed = request.form["breed"]
    age = request.form["age"]
    owner_first_name = request.form["owner_first_name"]
    owner_last_name = request.form["owner_last_name"]
    owner_contact_number = request.form["owner_contact_number"]
    dog = Dog(name, breed, age, owner_first_name, owner_last_name, owner_contact_number, id)
    dog_repository.update(dog)
    return redirect("/dogs")


# DELETE dog
@dogs_blueprint.route("/dogs/<id>/delete", methods=["POST"])
def delete_dog(id):
    dog_repository.delete(id)
    return redirect("/dogs")


# create new dog
# new
@dogs_blueprint.route("/dogs/new")
def new_dog():
    return render_template("/dogs/new.html")


# SAVE new dog
@dogs_blueprint.route("/dogs", methods=["POST"])
def create_dog():
    name = request.form["name"]
    breed = request.form["breed"]
    age = request.form["age"]
    owner_first_name = request.form["owner_first_name"]
    owner_last_name = request.form["owner_last_name"]
    owner_contact_number = request.form["owner_contact_number"]
    new_dog = Dog(name, breed, age, owner_first_name, owner_last_name, owner_contact_number)
    dog_repository.save(new_dog)
    return redirect("/dogs")