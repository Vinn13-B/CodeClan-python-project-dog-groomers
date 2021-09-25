# controller and routes for appointments

from flask import Blueprint, Flask, redirect, render_template, request

from models.appointment import Appointment
from models.dog import Dog
import repositories.appointment_repository as appointment_repository
import repositories.dog_repository as dog_repository

appointments_blueprint = Blueprint("appointments", __name__)