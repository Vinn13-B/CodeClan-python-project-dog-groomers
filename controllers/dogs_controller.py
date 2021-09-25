# controller and routes for dogs

from flask import Blueprint, Flask, redirect, render_template, request

from models.dog import Dog
from models.appointment import Appointment
import repositories.dog_repository as dog_repository
import repositories.appointment_repository as appointment_repository

dogs_blueprint = Blueprint("dogs", __name__)