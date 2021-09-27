# controller and routes for owners

from flask import Blueprint, Flask, redirect, render_template, request

from models.dog import Dog
from models.appointment import Appointment
from models.groomer import Groomer
from models.owner import Owner

import repositories.dog_repository as dog_repository
import repositories.appointment_repository as appointment_repository
import repositories.groomer_repository as groomer_repository
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)


# SELECT ALL owners
# index
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners=owners)


# SELECT owner by id
# show
@owners_blueprint.route("/owners/<id>")
def show_owner(id):
    owner = owner_repository.select(id)
    dogs = dog_repository.select_all()
    return render_template("owners/show.html", owner=owner, dogs = dogs)


# EDIT owner
# edit
@owners_blueprint.route("/owners/<id>/edit", methods=["POST"])
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template("owners/edit.html", owner=owner)


# UPDATE groomer
@owners_blueprint.route("/owners/<id>", methods=["POST"])
def update_owner(id):
    name = request.form["name"]
    contact_number = request.form["contact_number"]
    owner = Owner(name, contact_number, id)
    owner_repository.update(owner)
    return redirect("/owners")


# DELETE owner
@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect("/owners")


# create new owner
# new
@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template("/owners/new.html")


# SAVE new owner
@owners_blueprint.route("/owners", methods=["POST"])
def create_owner():
    name = request.form["name"]
    contact_number = request.form["contact_number"]
    new_owner = Owner(name, contact_number)
    owner_repository.save(new_owner)
    return redirect("/owners")