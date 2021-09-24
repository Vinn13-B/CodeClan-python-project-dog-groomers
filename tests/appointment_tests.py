# setting up Tests for Appointment class, testing each required object in class
# tests will also need to be created for required methods
# will then create class, objects and methods to pass each test
# for MVP, 'time' object will only offer 0800, 1000, 1200, 1400, 1600

import unittest

from models.appointment import Appointment

class TestAppointment(unittest.TestCase):

    def setUp(self):
        self.appointment= Appointment("0800", "Biscuits")
        self.time_pass = "0800"
        self.time_fail = "0900"

    def test_appointment_has_time(self):
        self.assertEqual("0800", self.appointment.time)

    def test_appointment_has_dog(self):
        self.assertEqual("Biscuits", self.appointment.dog)

    def test_check_time_pass(self):
        self.assertEqual(None, Appointment.check_time(self.time_pass))

    def test_check_time_fail(self):
        self.assertEqual("This time is unavailable", Appointment.check_time(self.time_fail))
