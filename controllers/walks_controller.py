# controller and routes for appointments

from flask import Blueprint, Flask, redirect, render_template, request

from models.appointment import Appointment
from models.dog import Dog
from models.groomer import Groomer
from models.walk import Walk

import repositories.appointment_repository as appointment_repository
import repositories.dog_repository as dog_repository
import repositories.groomer_repository as groomer_repository
import repositories.walk_repository as walk_repository

walks_blueprint = Blueprint("walks", __name__)


# SELECT ALL appointments
# index
@walks_blueprint.route("/walks")
def walks():
    walks = walk_repository.select_all()
    return render_template("walks/index.html", walks=walks)


# SELECT walk by id
# show
@walks_blueprint.route("/walks/<id>")
def show_walk(id):
    walk = walk_repository.select(id)
    return render_template("walks/show.html", walk=walk)


# EDIT walk
# edit
@walks_blueprint.route("/walks/<id>/edit", methods=["POST"])
def edit_walk(id):
    walk = walk_repository.select(id)
    dogs = dog_repository.select_all()
    return render_template("walks/edit.html", walk=walk, dogs=dogs)


# UPDATE walk
@walks_blueprint.route("/walks/<id>", methods=["POST"])
def update_walk(id):
    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    dog_id = request.form["dog_id"]
    dog = dog_repository.select(dog_id)
    walk = Walk(date, time, capacity, dog, id)
    walk_repository.update(walk)
    return redirect("/walks")


# DELETE appointment
@walks_blueprint.route("/walks/<id>/delete", methods=["POST"])
def delete_walk(id):
    walk_repository.delete(id)
    return redirect("/walks")


# create new walk
# new
@walks_blueprint.route("/walks/new")
def new_walk():
    dogs = dog_repository.select_all()
    return render_template("/walks/new.html", dogs=dogs)


# SAVE new walk
@walks_blueprint.route("/walks", methods=["POST"])
def create_walk():
    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["time"]
    dog_id = request.form["dog_id"]
    dog = dog_repository.select(dog_id)
    new_walk = Walk(date, time, capacity, dog)
    walk_repository.save(new_walk)
    return redirect("/walks")


# SELECT walks by date
@walks_blueprint.route("/walks/today")
def walk_date():
    walks = walk_repository.today()
    return render_template("/walks/today.html", walks=walks)


# SELECT walks by date range
@walks_blueprint.route("/walks/dates", methods=["POST"])
def walks_date_range():
    date_from = request.form["date_from"]
    date_to = request.form["date_to"]
    walks = walk_repository.date_range(date_from, date_to)
    dogs = dog_repository.select_all()
    return render_template("/walks/dates.html", walks=walks, dogs=dogs)